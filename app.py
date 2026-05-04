from flask import Flask, render_template, request
import requests
import anthropic
from dotenv import load_dotenv
import os
import markdown

load_dotenv()
app = Flask(__name__)
cliente = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def recolectar_datos(dominio):
    dns = requests.get(f"https://api.hackertarget.com/dnslookup/?q={dominio}").text
    hosts = requests.get(f"https://api.hackertarget.com/hostsearch/?q={dominio}").text
    geo = requests.get(f"https://api.hackertarget.com/geoip/?q={dominio}").text
    return dns, hosts, geo

def analizar_con_ia(dominio, dns, hosts, geo):
    respuesta = cliente.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Sos un analista de ciberseguridad explicándole a alguien sin conocimientos técnicos qué encontraste sobre el dominio {dominio}.

Analizá cada sección y explicá en español simple y claro:

**🌐 DNS — ¿Cómo está configurado el dominio?**
Explicá qué significan los registros DNS encontrados, en palabras simples.

**🔗 Subdominios — ¿Qué secciones tiene este sitio?**
Listá y explicá para qué sirve cada subdominio encontrado.

**📍 Ubicación — ¿Dónde están los servidores?**
Explicá dónde está alojado el sitio y qué significa eso.

**⚠️ Observaciones — ¿Hay algo llamativo?**
Mencioná cualquier cosa interesante o sospechosa que encontraste.

**📋 Resumen general**
Un párrafo simple explicando todo, como si le hablaras a alguien que nunca oyó hablar de internet.

Información recolectada:
DNS:
{dns}

Subdominios:
{hosts}

Geolocalización:
{geo}

Usá lenguaje simple, evitá jerga técnica sin explicación, y sé detallado pero claro."""
        }]
    )
    return markdown.markdown(respuesta.content[0].text)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    dominio = None
    error = None
    dns = hosts = geo = None

    if request.method == "POST":
        dominio = request.form.get("dominio", "").strip()
        if dominio:
            try:
                dns, hosts, geo = recolectar_datos(dominio)
                resultado = analizar_con_ia(dominio, dns, hosts, geo)
            except Exception as e:
                error = f"Error: {str(e)}"

    return render_template("index.html",
        resultado=resultado,
        dominio=dominio,
        dns=dns,
        hosts=hosts,
        geo=geo,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
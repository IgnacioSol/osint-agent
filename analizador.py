import anthropic
from dotenv import load_dotenv
import os

# Cargar la API key
load_dotenv()
cliente = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Leer el reporte
dominio = input("Ingresá el dominio del reporte a analizar: ")
nombre_archivo = f"reporte_{dominio}.txt"

with open(nombre_archivo, "r") as archivo:
    reporte = archivo.read()

# Analizar con IA
print("\nAnalizando con IA...\n")

respuesta = cliente.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""Sos un analista de ciberseguridad. Analizá esta información OSINT del dominio {dominio} y explicá en español:
1. Qué infraestructura tiene
2. Dónde está alojado
3. Si hay algo llamativo o sospechoso

Información:
{reporte}"""
        }
    ]
)

print("=== ANÁLISIS IA ===")
print(respuesta.content[0].text)


# Guardar en archivo
nombre_archivo = f"reporte_de_laIAsobre:{dominio}.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(f"informe de: {dominio}\n\n")
    archivo.write(respuesta.content[0].text)
print(f"\nReporte guardado en {nombre_archivo}")



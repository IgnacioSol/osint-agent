import requests

dominio = input("Ingresá un dominio: ")

print(f"cargando {dominio}.")
print(f"cargando {dominio}..")
print(f"cargando {dominio}...")


# DNS lookup
url_dns = f"https://api.hackertarget.com/dnslookup/?q={dominio}"
respuesta_dns = requests.get(url_dns)

# IP del dominio
url_ip = f"https://api.hackertarget.com/hostsearch/?q={dominio}"
respuesta_ip = requests.get(url_ip)

# Geolocalización de IP
url_geo = f"https://api.hackertarget.com/geoip/?q={dominio}"
respuesta_geo = requests.get(url_geo)

# Mostrar resultados
print("=== DNS ===")
print(respuesta_dns.text)

print("=== HOSTS ===")
print(respuesta_ip.text)
print("=== GEOLOCALIZACIÓN ===")
print(respuesta_geo.text)

# Guardar en archivo
nombre_archivo = f"reporte_{dominio}.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(f"Reporte OSINT: {dominio}\n\n")
    archivo.write("=== DNS ===\n")
    archivo.write(respuesta_dns.text)
    archivo.write("\n=== HOSTS ===\n")
    archivo.write(respuesta_ip.text)
    archivo.write("\n=== GEOLOCALIZACIÓN ===\n")
    archivo.write(respuesta_geo.text)

print(f"\nReporte guardado en {nombre_archivo}")



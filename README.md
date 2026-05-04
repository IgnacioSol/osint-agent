# Agente OSINT con IA

Herramienta de inteligencia de fuentes abiertas (OSINT) que recolecta información pública sobre dominios y la analiza automáticamente usando inteligencia artificial (Claude de Anthropic).

## ¿Qué hace?

- Consulta información DNS del dominio
- Mapea subdominios asociados
- Geolocaliza los servidores
- Genera un análisis automático con IA explicando los hallazgos

## Tecnologías

- Python 3
- Anthropic Claude API
- HackerTarget API
- python-dotenv

## Uso

1. Cloná el repositorio
2. Creá un archivo `.env` con tu API key de Anthropic
3. Instalá las dependencias: `pip install -r requirements.txt`
4. Corré la recolección: `python3 whois_lookup.py`
5. Corré el análisis: `python3 analizador.py`

## Autor

Ignacio Solano M — Estudiante de Ciberseguridad en la universidad Fidelitas.

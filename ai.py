import requests
import os

def consultar_ia(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-tiny",   # MODELO GRATIS
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=20)
        respuesta = response.json()

        return respuesta["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error al consultar la IA: {e}"

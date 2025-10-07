import streamlit as st
import requests

st.title("Información y Curiosidades sobre Gatos y Perros")

API_CAT = "https://api.thecatapi.com/v1"
API_DOG = "https://api.thedogapi.com/v1"


HEADERS = {
    "x-api-key": "live_5frbqoYMyS64M7Txgbc0WEs0O9u8rIuhwfe2aAhyM5hAjqRoyBejrFvfvN7P5St9"
}

# Selección de especie
especie = st.radio("Elige la especie:", ("Gatos", "Perros"))

def obtener_razas(url):
    response = requests.get(f"{url}/breeds", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def mostrar_info_raza(raza, url):
    st.header(raza['name'])
    st.write(raza.get('description', 'Descripción no disponible.'))
    # Obtener imagen si existe
    imagen_id = raza.get('reference_image_id')
    if imagen_id:
        img_url = f"{url}/images/{imagen_id}"
        img_response = requests.get(img_url, headers=HEADERS)
        if img_response.status_code == 200:
            img_data = img_response.json()
            st.image(img_data.get('url'), use_column_width=True)

if especie == "Gatos":
    razas = obtener_razas(API_CAT)
else:
    razas = obtener_razas(API_DOG)

nombres_razas = [r['name'] for r in razas]
raza_seleccionada = st.selectbox(f"Selecciona una raza de {especie.lower()}:", nombres_razas)

if raza_seleccionada:
    raza_info = next((r for r in razas if r['name'] == raza_seleccionada), None)
    if raza_info:
        mostrar_info_raza(raza_info, API_CAT if especie == "Gatos" else API_DOG)


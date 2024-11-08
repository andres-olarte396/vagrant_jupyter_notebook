import os
import openai
import json
from PIL import Image

# Configura tu clave API de OpenAI
openai.api_key = 'sk-XXXXXXXX'

# Configura el directorio de imágenes
image_directory = "/vagrant/data/images"

print(f"Iniciando en: {image_directory}")

# Función para generar una descripción con IA de una imagen
def describe_image(image_path):
    try:
        # Carga la imagen para obtener detalles (opcional)
        with Image.open(image_path) as img:
            img_details = f"La imagen tiene un tamaño de {img.size[0]}x{img.size[1]} píxeles."
        
        # Describe la imagen usando el modelo de IA de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente que proporciona descripciones detalladas de imágenes."
                },
                {
                    "role": "user",
                    "content": f"Describe detalladamente el contenido de esta imagen y proporciona enlaces informativos sobre el tema: {img_details}"
                }
            ],
            max_tokens=100
        )
        
        description = response['choices'][0]['message']['content'].strip()
     
        return {
            "ruta": image_path,
            "descripcion": description
        }
    
    except Exception as e:
        print(f"Error al procesar {image_path}: {e}")
        return None

# Procesa cada imagen en el directorio
def generate_json_for_images(directory):
    image_descriptions = []
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            print(f"Imagen: {image_path}")
            description = describe_image(image_path)
            if description:
                image_descriptions.append(description)
    
    # Guarda los resultados en un archivo JSON
    with open("descripciones_imagenes.json", "w", encoding='utf-8') as json_file:
        json.dump(image_descriptions, json_file, ensure_ascii=False, indent=4)
    
    print("Archivo JSON generado exitosamente.")

# Ejecuta la función para generar el JSON
generate_json_for_images(image_directory)

import io
import os
from google.cloud import vision
from google.cloud.vision_v1 import types

# Configurar la credencial
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\Semestre enero-junio-2024\IA\proyecto_ocr\ocrinteligenci-a8d422fc4a52.json'

def detect_text(path):
    """Detectar texto en la imagen."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print('Texto detectado:')
    for text in texts:
        print('\n"{}"'.format(text.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    detect_text('D:\Semestre enero-junio-2024\IA\proyecto_ocr\credencial1.jpg')

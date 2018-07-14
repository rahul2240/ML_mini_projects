import pytesseract
from PIL import Image
import requests
from io import BytesIO

img = 'https://codelabs.developers.google.com/codelabs/mobile-vision-ocr/img/c5134dae01ad22a5.png'
img = requests.get(img) 
img = Image.open(BytesIO(img.content)) 
text = pytesseract.image_to_string(img)

print text

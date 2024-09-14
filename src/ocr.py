import pytesseract
from PIL import Image

def get_image_to_text(img):

    img = Image.open(img)

    text = pytesseract.image_to_string(img)

    return text


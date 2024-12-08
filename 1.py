import pytesseract
from PIL import Image 

# Set the path for tesseract (for macOS)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
# Open the image file
img = Image.open('1.jpg')

# Perform OCR to extract text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

text=pytesseract.image_to_string(r"C:\Users\siva\Desktop\first\ONE.jpg")

f = open("recognized.txt", "w")

f.write(text)

f.close()
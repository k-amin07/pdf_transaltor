import pdfplumber
from deep_translator import GoogleTranslator

with pdfplumber.open("./sample.pdf") as pdf_file:
    pdf_pages = pdf_file.pages
    for i in range(len(pdf_pages)):
        page_text = pdf_pages[i].extract_text(x_tolerance=3, y_tolerance=3)
        print(page_text)
        translated_text = GoogleTranslator(source='auto', target='ur').translate(page_text)
        print(translated_text)
        print('\n')

import PyPDF2
import re
import tabula

pdf_file = open("pf1n3-2016.pdf", "rb")

# le o pdf
pdf = PyPDF2.PdfReader(pdf_file)

paginas = len(pdf.pages)
# print(paginas)

# extrair da primeira pagina
pagina1 = pdf.pages[0]

text_fomatado_page1 = ''.join(pagina1.extract_text())
# print(text_fomatado_page1)

# questoes separadas
list_separados = []
for index in range(1,5):
    print(index)
    text_pagina1_separado = text_fomatado_page1.split(f"{index}.")
    list_separados.append(text_pagina1_separado)
for i in lis:
    print(i)
    print('------------------------------------------------------------------')
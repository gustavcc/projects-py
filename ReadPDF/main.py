import PyPDF2

enem_bin = open('ENEM2022.pdf', 'rb')

pdf = PyPDF2.PdfFileReader(enem_bin)

num_pag = pdf.getNumPages()
print(num_pag)
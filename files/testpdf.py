from PyPDF2 import PdfReader

reader = PdfReader("./files/NDA.pdf")

# Listo para Almacenar el texto
lista_texto = []

for page in reader.pages:
    extracted_text = page.extract_text()
    if extracted_text:
        lista_texto.append(extracted_text)

texto = "\n".join(lista_texto).encode('utf-8')

print(texto)
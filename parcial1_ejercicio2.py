# Parcial 1
# Ejercicio 2
# Israel Hernandez

import Crypto.Random
import Crypto.Util.number 
from Crypto.Util.number import bytes_to_long, long_to_bytes
import hashlib
from PyPDF2 import PdfReader

e = 65537

#ALice
pA = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Alice pA: ', pA)
qA = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Alice qA: ', qA)

#Bob
pB = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Bob pB: ', pB)
qB = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Bob qB: ', qB)

#AC
pAC = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Bob pB: ', pAC)
qAC = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print('\n', 'RSA - Primo de Bob qB: ', qAC)

# Calculamos la llave publica de alice nA = pA * qA
nA = pA * qA

print('\n', 'RSA - nA: ', nA)

# Calcular la llave Privada de Alice
phiaA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiaA)

print('\n', 'Llave privada Alice dA: ', dA)

# Calculamos la llave publica de Bob nA = pA * qA
nB = pB * qB

print('\n', 'RSA - nB: ', nB)

# Calcular la llave Privada de Bob
phiaB = (pB - 1) * (qB - 1)

dB = Crypto.Util.number.inverse(e, phiaB)

print('\n', 'Llave privada Bob dB: ', dB)

# Calculamos la llave publica de AC nAC = pAC * qAC
nAC = pAC * qAC

print('\n', 'RSA - nAC: ', nAC)

# Calcular la llave Privada de AC
phiaAC = (pAC - 1) * (qAC - 1)

dAC = Crypto.Util.number.inverse(e, phiaAC)

print('\n', 'Llave privada AC dAC: ', dAC)



reader = PdfReader("./files/NDA.pdf")

# Listo para Almacenar el texto
lista_texto = []

# Recorrer cada página del PDF
for page in reader.pages:
    # Extraer el texto de la página
    extracted_text = page.extract_text()
    if extracted_text:
        lista_texto.append(extracted_text)


# Unir todos los textos con un salto de línea
text = "\n".join(lista_texto)


# Generamos el HASH del mensaje
hM = int.from_bytes(hashlib.sha256(text.encode('utf-8')).digest(), byteorder='big')
print("\n", "HASH de hM: ", hex(hM))

# Firmamos el HASH usando la llave privada de Alice y se lo enviamos a AC
sA = pow(hM, dA, nA)
print("\n", "Firma: ", sA)

# AC Verifica la firma de Alice usando la llave Publica de Alice
hM1 = pow(sA, e, nA)
print("\n", "HASH de hM1: ", hex(hM))

# Verificamos
if hM == hM1:
    print("\n", "Firma Valida: ", hM==hM1, "\n")
else:
    print("Error en la firma electronica")

# Firmamos el HASH usando la llave privada de AC y se lo enviamos a Bob
sAC = pow(hM, dAC, nAC)
print("\n", "Firma: ", sAC)

# Bob Verifica la firma de AC usando la llave Publica de AC
hM2 = pow(sAC, e, nAC)
print("\n", "HASH de hM1: ", hex(hM2))

# Verificamos
if hM == hM2:
    print("\n", "Firma Valida: ", hM==hM2, "\n")
else:
    print("Error en la firma electronica")




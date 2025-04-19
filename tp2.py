numero = 101011
suma = 0

#obtengo el indice del digito empezando desde la derecha
for i in range(len(str(numero))):
    digito = numero % 10
    numero = numero // 10
    if digito == 1:
        suma += 2 ** i
    print(digito, i)
print(f"El número en decimal es: {suma}")

numero = 725
suma = 0

#obtengo el indice del digito empezando desde la derecha
for i in range(len(str(numero))):
    digito = numero % 10
    numero = numero // 10
    suma += (8 ** i) * digito
    print(digito, i)
print(f"El número en decimal es: {suma}")


def numero_a_decimal(numero, base):
    suma = 0
    for i in range(len(str(numero))):
        digito = numero % 10
        numero = numero // 10
        suma += (base ** i) * digito
    return suma

numero = 101011
print(numero_a_decimal(numero, 2))
numero = 725
print(numero_a_decimal(numero, 8))

def hexadecimal_a_decimal(numero,base):
    suma = 0
    for i in range(len(numero)):
        digito = numero[-1-i]
        if digito.isdigit() == False:
            if digito == 'A':
                digito = 10
            elif digito == 'B':
                digito = 11
            elif digito == 'C':
                digito = 12
            elif digito == 'D':
                digito = 13
            elif digito == 'E':
                digito = 14
            elif digito == 'F':
                digito = 15
        else:
            digito = int(digito)
        print(f"la base es {base} y el digito es {digito}")
        print(f"la base es {base}**{i} da {base ** (i)}")
        suma += (base ** i) * digito
    return suma
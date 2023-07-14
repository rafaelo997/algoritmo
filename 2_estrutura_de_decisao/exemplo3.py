numero1 = 8
numero2 = 10
numero3 = 5

if numero1 > numero2:
    auxiliar = numero1
    numero1 = numero2
    numero2 = auxiliar

if numero2 > numero3:
    auxiliar = numero2
    numero2 = numero3
    numero3 = auxiliar

if numero1 > numero2:
    auxiliar = numero1
    numero1 = numero2
    numero2 = auxiliar

print(f"{numero1} <= {numero2} <= {numero3}")

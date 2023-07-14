# faça um algoritmo que leia 
# três números e mostre o maior deles.
numero1 = int(input("Digite o primeiro número: "))
maior = numero1

numero2 = int(input("Digite o segundo número: "))
if numero2 > maior:
    maior = numero2

numero3 = int(input("Digite o terceiro número: "))
if numero3 > maior:
    maior = numero3

print(f"O maior número é: {maior}")

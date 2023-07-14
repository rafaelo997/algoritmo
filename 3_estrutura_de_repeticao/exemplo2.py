# faça um algoritmo que leia 05 números e 
# informe o maior número.
contador = 1
maior = 0

# enquanto o contador for menor ou igual a 5
while contador <= 5:
    # solicita o número
    numero = int(input(f"Digite o {contador}º número: "))
    
    # verifica se o número é maior que o maior
    if contador == 1 or numero > maior: 
        maior = numero
    
    # incrementa o contador
    contador += 1

# imprime o maior número
print(f"O maior número é {maior}")

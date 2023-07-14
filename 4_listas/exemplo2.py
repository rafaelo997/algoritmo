numeros = [] # cria a lista de números
pares = [] # cria a lista de pares
impares = [] # cria a lista de ímpares

# cria um laço de para pegar os 20 numeros
for item in range(20):
    # pega o número digitado pelo usuário
    numero = int(input(f"Digite o {item + 1}º número: "))
    # adiciona o número na lista de números
    numeros.append(numero)
    # verifica se o número é par
    par = numero % 2 == 0
    if par: # se for par
        # adiciona o número na lista de pares
        pares.append(numero)
    else: # se for ímpar
        # adiciona o número na lista de ímpares
        impares.append(numero)

print("Lista de números:", numeros) # imprime a lista de números
print("Lista de pares:", pares) # imprime a lista de pares
print("Lista de ímpares:", impares) # imprime a lista de ímpares

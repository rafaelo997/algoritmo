# inicializacao da variavel tabuada
tabuada = 0

# solicitando um valor de tabuada valido
while tabuada < 1 or tabuada > 10:
    tabuada = int(input("Digite um número: "))

# exibindo a tabuada
print(f"Tabuada de {tabuada}")
for numero in range(1, 11):
    resultado = tabuada * numero
    print(f"{tabuada} x {numero} = {resultado}")

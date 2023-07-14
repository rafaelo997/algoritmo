def questao1(numero):
    resultado = ""
    for n in range(1, numero + 1):
        for i in range(1, n + 1):
            resultado += f"{str(n)} "
        resultado += "\n"
    return resultado
 #######################

teste = int(input("Digite um número: "))
print(questao1(teste))

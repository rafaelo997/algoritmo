# solicita o numero 1
nota1 = float(input("Digite a nota 1: "))

# solicita o numero 2
nota2 = float(input("Digite a nota 2: "))

# solicita o numero 3
nota3 = float(input("Digite a nota 3: "))

# a media dos numeros
media = (nota1 + nota2 + nota3) / 3

# verifica se a media é maior ou igual a 70
aprovado = media >= 60
reprovado = media < 30

situacao = "RECUPERAÇÃO"

# verifica se aprovado
if aprovado:
    situacao = "APROVADO"
elif reprovado:
    situacao = "REPROVADO"

# imprime o resultado
print(f"A média dos números é: {media:.2f} - {situacao}")

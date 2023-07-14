frutas = ["maçã", "banana", "laranja", "melancia", "uva", "banana"]

for fruta in frutas:
    frutas[frutas.index(fruta)] = str(fruta)

frutas.sort()

print(frutas)

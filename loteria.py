arquivo = open("resultados_loteria.txt", "r")
texto = arquivo.readlines()
dados =[]
repeticoes = []
mais = []
menos = []

for frase in texto:
    frase = frase.strip('\n')
    frase = frase.split('\t')
    for x in frase:
        dados.append(int(x))
    dados.sort()
for x in range (60):
    repeticoes.append([dados.count(x+1),x+1])
    print("o numero ",x+1," aparece ",dados.count(x+1), " vezes ")
print("quantidade que cada numero repetiu")
for i in repeticoes:
    print(i)
repeticoes.sort()
for i in range(6):
    mais.append(repeticoes[i][1])
mais.sort()
print("numero que mais sairam", mais)
repeticoes.sort(reverse=True)
for i in range (6):
    menos.append(repeticoes[i][1])
menos.sort()
print("numero que menos sairam", menos)

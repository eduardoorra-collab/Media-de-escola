prova1 = float(input("Digite sua nota P1: "))

prova2 = float(input("Digite sua nota P2: "))

trabalho = float(input("Digite sua nota Trabalho: "))

licao = float(input("Digite sua nota da Lição: "))

comportamento = float(input("Digite sua nota de comportamento: "))

media = (prova1 + prova2 + trabalho + licao + comportamento) / 5

if (media >= 6):
    print("passo")
else:
    print("reprovo")

print(media)
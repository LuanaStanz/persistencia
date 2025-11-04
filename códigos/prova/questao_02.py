import pandas as pd

#series com nomes como indices e calores
associados = pd.Series([12000, 17500, 14300, 16000, 19500], index=["Luca Brasi ", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"])
sum = associados.sum()
print(f"total arrecadado na semana: {sum}\n")

media = associados.mean()
print(f"média das receitas: {media}\n")

mais = associados[associados == associados.max()].index[0]
print(f"Nome do que mais arrecadado: {mais}\n")

#associados que arrecadaram acima da média, mostrando o nome e o valor correspondente (use operação booleana sobre a própria Series).
acima_media = associados[associados > media]
print("Associados que arrecadaram acima da média:")
for nome, valor in acima_media.items():
    print(f"Nome: {nome}")
    print(f"{valor}\n")
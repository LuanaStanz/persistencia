#pip install bs4
import requests
from bs4 import BeautifulSoup # pulling data from HTML and XML

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

#calcular quandas vezes jogador 1 venceu o pedra papel tesoura
table = soup.find("table")
jogadas = table.find_all("td")
j1 = table.find_all("td",{"class":"j1"})
j2 = table.find_all("td",{"class":"j2"})
j1 = [td.get_text() for td in j1]
j2 = [td.get_text() for td in j2]

contador = 0
for i in range(len(j1)):
    if (j1[i] == "pedra" and j2[i] == "tesoura") or (j1[i] == "papel" and j2[i] == "pedra") or (j1[i] == "tesoura" and j2[i] == "papel"):
        contador += 1
    
print(j1)
print(j2)

print(f"Jogador 1 venceu {contador} vezes")

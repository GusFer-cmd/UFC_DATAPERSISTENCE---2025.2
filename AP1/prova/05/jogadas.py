from bs4 import BeautifulSoup

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table",{"id":"jogadas"})
rows = table.find_all("tr")[1:]

vitorias = 0

for row in rows:
    jogada1 = row.find("td", {"class": "jogada1"}).text.strip()
    jogada2 = row.find("td", {"class": "jogada2"}).text.strip()
            
    if ((jogada1 == "Pedra" and jogada2 == "Tesoura")
        or (jogada1 == "Tesoura" and jogada2 == "Papel")
        or (jogada1 == "Papel" and jogada2 == "Pedra")):
        vitorias = 1

        print(f"Jogador 1 venceu{vitorias} vez. Parabéns!")
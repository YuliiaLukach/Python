"""
Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň (jedná se o právní předpisy). Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo, později každé 4. slovo atd., až se text naučí zpaměti. Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zaměnit.
"""

with open("lorem.txt") as f:
  text = f.read()
f.closed

text = text.replace("\n", "#")

seznam = []
seznam = text.split(" ")
vysledek = []
interpunkce = ".,?!-;\""

for i in range(0, len(seznam)):
  slovo = seznam[i]
  slovoUpraveno = ""
  if ((i + 1) % 5 == 0):
    for pismeno in slovo:
      if pismeno not in interpunkce:
        slovoUpraveno += "*"
      else:
        slovoUpraveno += pismeno
    vysledek.append(slovoUpraveno)
  else:
    vysledek.append(slovo)

s = " ".join(vysledek)
s = s.replace("#", "\n")
print(s)


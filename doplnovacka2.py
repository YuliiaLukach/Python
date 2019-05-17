"""
Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň (jedná se o právní předpisy). Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo, později každé 4. slovo atd., až se text naučí zpaměti. Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zaměnit.
----
Proveďte optimalizaci kódu programu "doplnovacka.py" tak, abys problém řešila s využitím vlastní funkce (vstupními parametry bude vložený text či název souboru, který se má načíst, a celé číslo představující, kolikáté slovo textu se má zaměnit za hvězdičky). Tuto optimalizovanou verzi nahraj do existujícího projektu na GitHubu. 

"""

def doplnovacka(lorem,cislo):
  with open(lorem) as f:
    text = f.read()
  f.closed

  text = text.replace("\n", "#")
  cislo = int(cislo)
  seznam = []
  seznam = text.split(" ")
  vysledek = []
  interpunkce = ".,?!-;\""

  for i in range(0, len(seznam)):
    slovo = seznam[i]
    slovoUpraveno = ""
    if ((i + 1) % cislo == 0):
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

doplnovacka("lorem.txt",2)

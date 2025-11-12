from num2words import num2words
import pynini

#je genere la grammaire des nombres en francais et anglais
gram_fr = [(str(i), num2words(i, lang='fr')) for i in range(0, 1001)]
mod_fr = pynini.string_map(gram_fr)

gram_en = [(str(i), num2words(i, lang='en')) for i in range(0, 1001)]
mod_en = pynini.string_map(gram_en)

#jenregistre le fichier FAR
# FR
with pynini.Far("numbers_fr.far", mode="w") as far:
    far["numbers"] = mod_fr

# EN
with pynini.Far("numbers_en.far", mode="w") as far:
    far["numbers"] = mod_en


#Je cree une fonction pour normaliser mon texte (en ecrivant mes chiffres en lettre en fonction de la langue)
def normaliser_texte(texte, lang="fr"):
  if lang == "fr":
    far = pynini.Far("numbers_fr.far")
  else:
    far = pynini.Far("numbers_en.far")
  fst = far["numbers"]

  words = texte.split()
  sortie = []

  for word in words:
    try:
      #si le mot correspond à un nombre, on le normalise
      normalized = pynini.shortestpath(word @ fst).string()
      sortie.append(normalized)
    except:
      #si cest pas le cas on le garde intact
      sortie.append(word)
  #on retourne la liste des mots (normalisé ou pas) en les separant par un espace
  return " ".join(sortie)


texte = input("Entrer votre texte: ")
result = normaliser_texte(texte)
print(f"Texte normalisé est: {result}")

          




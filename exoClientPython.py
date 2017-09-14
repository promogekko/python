from collections import namedtuple
import re

list = []
myFile = open("data.txt" , "r")
for x in myFile:
    list.append(x.rstrip())
list = list[2:]

newList = []
for x in list:
    newList.append(x.split(","))

product = namedtuple('Produit' , ['code' , 'type', 'fournisseur', 'date'])
tuplelist = []

for x in newList:
    tuplelist.append(product._make(x))

finalList = []
for x in tuplelist:
    m = re.search(r"([A-Z]{3})(\d{3})", x.code)
    if m is not None:
        finalList.append(x)

question = input('Entrer votre code produit ou tapez Entrer pour afficher tous les codes produits\n')
for produit in finalList:
    if question == produit.code:
         print(produit)
         exit()
    elif question == "":
        print(produit.code)

reponse = input('\nEntrer votre code\n')
for produit in finalList:
    if reponse  ==  produit.code:
        print(produit)
        exit()









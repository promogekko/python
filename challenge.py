#!/usr/local/bin/python3
from collections import namedtuple
import re

def askingProduct():
    for x in range(len(res)):
        print(res[x].Code)
    productCode = input("Selectionnez un code produit ?  ")
    if productCode == "":
        askingProduct()
    elif productCode == "exit":
        exit()
    else:
        return productCode

# utiliser une commande pour lire le fichier data.txt
file = open("data.txt", 'r').read()

# faire des recherches pour choisir le type de donnees Python pour stocker ces informations le plus facilement possible
outputList2,productList, res = [],[], []
outputList = file.split('\n')
metadata = outputList[:1]
metadata = metadata[0].split(',')
Produit = namedtuple('Produit', metadata)
outputList = outputList[2:len(file) - 1]

for x in outputList:
    outputList2.append(x.split('\''))

for x in outputList2:
    outputList = x[0].split(',')
    productList.append(Produit(outputList[0], outputList[1], outputList[2], outputList[3]))

# verifier que le code Produit est valide, il doit avoir 3 caracteres alpha  et  3 digits
for x in productList:
    if re.search(r"[A-Z]{3}\d{3}", x[0]) is not None:
        res.append(x)
# afficher une question pour chercher un code produit
# si la chaine de reponse a la question est la touche Enter, afficher tous les codes produits qui sont valides
productCode = askingProduct()
# on peut alors saisir un code produit et afficher ainsi toutes les donnees associees a ce produit
for x in res:
    if productCode == x[0]:
        print(x)

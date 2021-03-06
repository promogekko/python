# utiliser une commande pour lire le fichier data.txt
# faire des recherches pour choisir le type de donnees Python pour stocker ces informations le plus facilement possible
# verifier que le code Produit est valide, il doit avoir 3 caracteres alpha  et  3 digits
# afficher une question pour chercher un code produit
# si la chaine de reponse a la question est la touche Enter, afficher tous les codes produits qui sont valides
# on peut alors saisir un code produit et afficher ainsi toutes les donnees associees a ce produit

import re
from collections import namedtuple

Record = namedtuple('Rec',['code','desc','societe','date'])
Produits = []
F = open("data.txt","r")
data = F.readlines()
#print(data)
for x in range(2,len(data)):
    line = data[x].rstrip()

    items = line.split(',')
    #print(items)
    m = re.search(r"([A-Z]{3})(\d{3})", items[0])
    if m is not None:
        #print (items)
        Name_tuple = Record(*items)
        Produits.append(Name_tuple)

#print(Produits)
enter = input ("taper un code produit ou taper enter pour obtenir la liste des codes\n")
if enter is "":
    for x in Produits:
        print(x.code)
else:
    enter = enter.rstrip()
    for x in Produits:
        if x.code == enter:
            print(x.desc,x.societe,x.date)


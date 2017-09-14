import re
f=open('data.txt', 'r')

var1 = list()
for x in f:
    str1=str.rstrip(x)
    if str1 == "":
        break
    else:
        str1=str1.split(',')
        if None != re.search(r"(([a-zA-Z]{3})(\d{3}))", str1[0]):
            if ((len(str1[0]) == 6)):
                var1.append(str1)

while 1:
    print("Les commandes disponibles sont exit, help et saisir un code produit.")
    phrase = input("Quelle est votre commande ?\n")
    if phrase == "exit":
        break
    elif "help" in phrase:
        print("Les commandes disponibles sont exit (pour quitter), help(avoir de l'aide) \net saisir un code produit (3 lettres et 3 chiffres).")
    elif phrase == "":
        i = 0
        for x in var1:
            print(var1[i][0])
            i += 1
    elif None != re.search(r"(([a-zA-Z]{3})(\d{3}))", phrase):
        if  ((len(phrase) == 6)):
            o = 0
            for z in var1:
                if var1[o][0] == phrase:
                    print(var1[o])
                o += 1
            else:
                print("Ce code produit n'existe pas")
        else:
            print("Mauvaise commande merci de taper help")
    else:
         print("Mauvaise commande merci de taper help")
f.close()
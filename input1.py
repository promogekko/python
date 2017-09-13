nom = input("ton nom ? ")
age = input("age ? ")
age = float(age)
print("\t Nom :", nom, "\t Age :", age)
## bonnes pratiques :
nom = input("ton nom ? ") # pour une chaine
age = float(input("age ? ")) # sinon : transtyper explicitement
print("{}\n\t Nom : {}\t Age : {}".format("-"*40, nom, age))
from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("Pratchett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi"),
        Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
        Book("Turner", "The Thief", "fantasy"),
        Book("Phillips", "Preston Diamond", "western"),
        Book("Phillips", "Twice Upon A Time", "scifi"),
        ]

fantasy_authors = {
        b.author for b in books if b.genre == 'fantasy'}
#print(fantasy_authors)

# -------------------------------------------
S = [x**2 for x in range(10)]
ST= {x**2 for x in range(10)}
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]

#print(S)
#print(set(ST))
#print(V)
#print(M)

#-------------------- yield -------------
def creerGenerateur():
        mylist = range(3)
        for i in mylist:
                yield i*i

generateur = creerGenerateur()
#print (generateur)
#for i in generateur:
#        print(i)

#----------------------- passage d'un tuple
def somme(*args):
        resultat = 0
        for nombre in args:
                resultat += nombre
        return resultat

#print("-"*40)
#print(somme(23))
#print("\n", "-"*40)
#print(somme(-10, 13))
#print("\n", "-"*40)
#print(somme(23, 42, 13))
#print("\n", "-"*40)
#print(somme(-10.0, 12))

#---------------------- decompression d'un tuple
# fonction
def somme(a, b, c):
        return a+b+c
# programme principal ----
sequence = (2, 4, 6)
#print(somme(*sequence))

# ------------------passage d'un dictionnaire

# fonction
def unDictionnaire(**kargs):
        return kargs

# programme principal -----------------------------------------------
#print(" appel avec des parametres nommes ".center(60, '-'))
#print(unDictionnaire(a=23, b=42))
#print(" appel avec un dictionnaire decompresse ".center(60, '-'))
mots = {'d':85, 'e':14, 'f':9}
#print(unDictionnaire(**mots))


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)


colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
#coloured_things = [ (x,y) for x in colours for y in things ]
#print(coloured_things)

coloured_thing =[]
for x in colours:
        for y in things:
                coloured_thing.append((x,y))
print(coloured_thing)



result_value = []
for i in "abc":
        for j in "de":
                result_value.append(i+j)
print(" boucle for ".center(50, '-'))
print(result_value, '\n')
rien = input('"Entree"')

result_val = [i+j for i in "abc" for j in "de"]
print(" forme ".center(50, '-'))
print(result_val)




ranks = {"ghost": 1, "habanero": 2, "cayenne": 3}
rank_dict = {rank: name for name,rank in ranks.items()}
len_set = [len(name) for name in rank_dict.values()]
len_set.sort()
print(rank_dict)
print(len_set)










names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
#names.sort(key=lambda x: len(x))
names.sort(key=lambda  x: len(x))

print(names)

def table(base, debut, fin, inc):
        """Affiche la table des <base>, de <debut> a <fin>, de <inc> en <inc>."""
        n = debut
        while n <= fin:
                print(n, 'x', base, '=', n*base)
                n += inc

# programme principal -----------------------------------------------
table(7, 7, 26, 2)











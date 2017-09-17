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
print(fantasy_authors)

# -------------------------------------------
S = [x**2 for x in range(10)]
ST= {x**2 for x in range(10)}
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]

print(S)
print(set(ST))
print(V)
print(M)

#-------------------- yield -------------
def creerGenerateur():
        mylist = range(3)
        for i in mylist:
                yield i*i

generateur = creerGenerateur()
print (generateur)
for i in generateur:
        print(i)




from collections import namedtuple

#Card = namedtuple('Card', ['rank', 'suit'])

class Card(namedtuple("Cards",'rank')):
    __slots__ = ()

    def __str__(self):
        return "type ={}".format(self.rank)

    def __format__(self, format_spec):
        return self.__str__()


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    #def __str__(self):
    #   return "{} : {}".format(self.cards.rank, self._cards.suit)

a = FrenchDeck()
print(len(a))
print(a[10])

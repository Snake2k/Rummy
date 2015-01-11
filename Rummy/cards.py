from random import shuffle

class Cards:
    def __init__(self):
        self.suits = ['S', 'C', 'D', 'H']
        self.rank  = {'A': 1, '2': 2,  '3': 3, '4': 4,\
                      '5': 5, '6': 6,  '7': 7, '8': 8, '9': 9, \
                      '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        self.deck = [j + i for i in self.suits for j in self.rank]
    def shuffle(self):
        shuffle(self.deck)

c = Cards()
print c.deck
c.shuffle()
print c.deck

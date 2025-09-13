import random

class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value
    def __str__(self):
        return self.face + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        self.suit = ["Spades","Clubs","Hearts","Diamonds"]
        self.face = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.play_index = 0


        for suit in self.suit:
            i = 0
            for i in range(len(self.face)):
                self.deck.append(Card(suit,self.face[i],self.value[i]))
              
    def print_deck(self):
            for card in self.deck:
                print(card.face + " of " + card.suit)
            print("---")
        
    def get_card(self):
            self.play_index += 1
            card = self.deck[self.play_index - 1]
            # print("You drew: " + str(card))
            return self.deck[self.play_index-1]

    def shuffle_Deck(self):
            random.shuffle(self.deck)
            self.play_index = 0

# deck = Deck()
# deck.shuffle_Deck()
# deck.print_deck()
# deck.get_card()



from random import randint
"""Class Cards: creates a deck of cards and then implements a method of drawing. In theory, you should not get duplicates.

However, in practice, I noticed this was not the case, so I had to implement another anti-duplicate feature in the director class."""
class Cards:
    def __init__(self):
        self.cards = []
        for i in range(13):
            self.cards.append(i + 1)
            
        self.last_card_drawn = 0
        
    def draw_card(self):
        card_index = randint(0, 12)
        is_same_card = True
        while is_same_card:
            drawn_card = self.cards[card_index]
            if drawn_card != self.last_card_drawn:
                is_same_card = False
        return drawn_card
          
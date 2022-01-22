from random import randint

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
            if drawn_card == self.last_card_drawn:
                is_same_card = False
        return drawn_card
          
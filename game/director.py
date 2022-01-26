from game.cards import Cards
class Director:
    def __init__(self):
        """Atributes:
        - score - will be updated whether the player wind or lose the round.
        - current_card - will display a random card after the player enters high or lower.
        - next_card - holds the next value of card to be compared to current_card
        - playing (boolean) - whether or not the game is being played.
        - deck - an instance of Cards from the Cards class
        - first_card (boolean) - determines whether or not this is the first card, so as to skip the initial 'play again' message
        - guess - The player's guess
        - incorrect_format - Handles a player typing something either than HI or LO"""
        self.score = 300
        self.current_card = ""
        self.next_card = ''
        self.playing = True
        self.deck = Cards()
        self.first_card = True
        self.guess = ''
        self.incorrect_format = False
    def start_game(self):
        """Starts the game by running the main game loop.
        
        """
        while self.playing:
            """Display the first card
            Get the input from the user
            output the next card
            display player's score
            Ask if the user wants to play again.
            """
            self.display_card()
            self.get_input()
            self.do_updates()
            self.give_output()
    def display_card(self):
        if self.first_card == True:
            self.current_card = self.deck.draw_card()
        print(f"Current card is {self.current_card}")
        
    def get_input(self):
        
        
        
        """
        Ask the user if they want to play again if the first card has already been resolved
        """
        if self.first_card == True:
            play = input("Play again? [y/n] ")
            self.is_playing = (play == "y")
            print()
            
        self.guess = input('Is the next card higher or lower? Enter HI or LO to guess: ').upper()
        
    
    def do_updates(self):
        self.incorrect_format = False
        self.first_card = False
        self.next_card = self.deck.draw_card()
        if self.guess == 'HI':
            if self.next_card > self.current_card:
                self.score += 100
            else:
                self.score -= 75
        elif self.guess == 'LO':
            if self.next_card < self.current_card:
                self.score += 100
            else:
                self.score -= 75
        else:
            self.incorrect_format = True
        self.current_card = self.next_card
            
    
    def give_output():
        pass
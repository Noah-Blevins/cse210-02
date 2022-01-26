from game.cards import Cards
class Director:
    def __init__(self):
        """Atributes:
        - score - will be updated whether the player wind or lose the round.
        - current_card - will display a random card after the player enters high or lower.
        - playing (boolean) - whether or not the game is being played."""
        self.score = 300
        self.current_card = ""
        self.playing = True
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
        pass
    def get_input():
        pass
    
    def do_updates():
        pass
    
    def give_output():
        pass
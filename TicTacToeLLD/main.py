from models.Player import Player
from models.OPiece import OPiece
from models.XPiece import XPiece
from Game import Game

def main():
    player1 = Player(name="Prafull",piece=OPiece())
    player2 = Player(name="Ranjan",piece=XPiece())
    players = [player1, player2]
    game = Game(3,players)
    game.play()


if __name__ == "__main__":
     main()




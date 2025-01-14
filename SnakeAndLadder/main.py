from models.Snake import Snake
from models.Ladder import Ladder
from models.Board import BoardI
from models.Player import Player
from Game import Game

def main():
    board = BoardI(10)
    board.set_moving_entity(8, Snake(2))
    board.set_moving_entity(3, Ladder(6))
    player1 = Player(1,"Prafull")
    player2 = Player(2,"Ranjan")
    players = [player1, player2]

    game = Game(board=board,players=players,dice_side=6)

    game.play()


if __name__== "__main__":
    main()



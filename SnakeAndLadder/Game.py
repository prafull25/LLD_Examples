from models.Board import BoardI
from models.Player import Player
from models.Dice import Dice
from typing import List
class Game:
    def __init__(self,board:BoardI,players : List[Player],dice_side):
            self.board = board
            if len(players)<2:
                raise ValueError("Player must be more than 1 !")
            self.players = players
            self.current_player_index = 0
            self.dice = Dice(dice_side)
            self.consecutive_six = 0
            self.last_rank = 1

    
    def switch_player(self, dice_result):
        # change player turn basis dice result.
        # if it's six, do not change .
        # if it's three consecutive sixes or not a six, change
        self.consecutive_six = 0 if dice_result != 6 else self.consecutive_six + 1
        if dice_result != 6 or self.consecutive_six == 3:
            if self.consecutive_six == 3:
                print("Changing turn due to 3 consecutive sixes")
            # self.current_player_index = (self.current_player_index +1)% len(self.players)
            self.get_next_player()
        else:
            print(f"One more turn for player {self.players[self.current_player_index].name} after rolling 6")
    
    def is_game_over(self):
        if self.last_rank != len(self.players):
            return False
        return True

    def can_move(self, curr_player, to_move_pos):
        if to_move_pos <= self.board.get_size() and curr_player.get_rank() == -1:
            return True
        return False
    
    def get_next_player(self):
        while True:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            if self.players[self.current_player_index].get_rank() == -1:
                return self.players[self.current_player_index]
            


    def move_player(self, curr_player:Player, next_pos):
        # Move player to next_pos
        curr_player.set_position(next_pos)
        if self.board.is_at_end_position(curr_player.get_position()):
            curr_player.set_rank(self.last_rank)
            self.last_rank += 1

    def play(self):
        while True:
            curr_player = self.players[self.current_player_index]
            _ = input(
                f"Player {self.players[self.current_player_index].name}, Press enter to roll the dice")
            dice_result = self.dice.roll()
            print(f'dice_result: {dice_result}')
            _next_pos = self.board.get_next_position(
                curr_player.get_position() + dice_result)
            if self.can_move(curr_player, _next_pos):
                self.move_player(curr_player, _next_pos)
            
            self.print_game_state()
            if self.is_game_over():
                last_player = self.get_next_player()
                last_player.rank = self.last_rank
                break
            self.switch_player(dice_result)
            
        self.print_game_result()


    def print_game_state(self):
        print('-------------game state-------------')
        for ix, _p in enumerate(self.players):
            print(f'Player: {ix+1}. {_p.name} is at pos {_p.get_position()}')
        print('-------------XXX-------------\n\n')
 
    def print_game_result(self):
        print('-------------final result-------------')
        for _p in sorted(self.players, key=lambda x: x.get_rank()):
            print(f'Player: {_p.name} , Rank: {_p.get_rank()}')
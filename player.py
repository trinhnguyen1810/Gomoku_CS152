import random
class Player:
    """
    A parent class representing a player in the Gomoku game.
    ---------------------
    Attribute:
       - player(str): The player's symbol
    
    """

    def __init__(self,player):
        self.player = player
    
    def get_move(self, game):
        pass

class ComputerPlayerEasy(Player):
    """
    A child class of the Player class representing a random moves generator
    ---------------------
    Attribute:
       - player(str): The player's symbol
    
    """
    def __init__(self, player):
        super().__init__(player)

    
    def get_move(self, game):
        if len(game.available_bounded_pos()) == 0:
            move = [6,6]
        else:
            move = random.choice(game.available_bounded_pos())
        game.mark_position(move, player=self.player, do_print=True)
        game.all_moves_comp.append(move)
        game.all_moves.append(move)
        return move

class SelfPlayer(Player):
    """
    A child class of the Player class representing a human player.
    ---------------------
    Attribute:
       - player(str): The player's symbol
    
    """
    
    def __init__(self, player):
        super().__init__(player)
    
    def get_move(self, game):
        input_val = None
        valid_move = False
        while not valid_move:
            player_input = input(f"It's {self.player}'s turn. Enter the game position in row/column form (eg: A4):")
            player_input = player_input.strip()
            input_val = self.parse_input(player_input)
            valid_move = game.mark_position(input_val, player=self.player, do_print=True)
        game.all_moves.append(input_val)
        return input_val
    
    def parse_input(self,player_input):
        #parsing input of users to get correct index
        try:
            row = player_input[0].upper()
            row = ord(row.upper()) - 65
            column = int(player_input[1:])-1
            return [int(row), column]
        except:
            return False, False


class ComputerPlayAI(Player): 
    """
    A child class of the Player class representing a computer AI agent.
    ---------------------
    Attribute:
       - player(str): The player's symbol
    
    """
    def __init__(self, player):
        super().__init__(player)
    def get_move(self, game):
        move = game.get_opt_move()
        game.mark_position(move, player=self.player, do_print=True)
        game.all_moves_comp.append(move)
        game.all_moves.append(move)
        return move

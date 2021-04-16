from models.game import Game
from models.player import Player


player_1 = Player("Umair","Scicoor")

player_2 = Player("John","Rock")

Game_01 = Game("first_game",player_1, player_2)


def play_game( player_1_gesture_selection, player_2_gesture_selection):

        if player_1_gesture_selection == 'Rock' and player_2_gesture_selection == 'Scicoor':
                
                return player_1.name
        elif player_1_gesture_selection== player_2_gesture_selection:
                return "Draw"




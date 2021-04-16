from models.game import Game
from models.player import Player


player_1 = Player("Umair","scissors")

player_2 = Player("John","Rock")

Game_01 = Game("first_game",player_1, player_2)


def play_game( player_1_gesture_selection, player_2_gesture_selection):

        for win_combination in Game_01.win_combination:
                if [player_1_gesture_selection,player_2_gesture_selection] == win_combination:
                        return player_1.name
                elif [player_2_gesture_selection, player_1_gesture_selection] == win_combination:
                        return player_2.name





from models.game import Game
from models.player import Player
from random import Random, randrange



player_1 = Player("Umair")
player_2 = Player("John")
computer_2 =Player("Robort_02")
Game_01 = Game("first_game",player_1, player_2)

selection_list = ['Rock','Scissor','Lizard', 'Spock','Paper']



def set_players_gesture( player_1_gesture_selection, player_2_gesture_selection):
        player_1.gesture_selection= player_1_gesture_selection
        player_2.gesture_selection= player_2_gesture_selection



def play_game( player_1_gesture_selection, player_2_gesture_selection):
        set_players_gesture(player_1_gesture_selection, player_2_gesture_selection)
        for win_combination in Game_01.win_combination:
                if [player_1_gesture_selection,player_2_gesture_selection] == win_combination:
                        return player_1.name
                elif [player_2_gesture_selection, player_1_gesture_selection] == win_combination:
                        return player_2.name



def set_computer_game(player_01_name,gesture_selection):
        player_3 = Player(player_01_name)
        player_3.gesture_selection= gesture_selection
        select_randon_gesture()
        Game_02 = Game("Second_game",player_1, computer_2)
        return Game_02



def select_randon_gesture():
        index_number = randrange(4)
        computer_2.gesture_selection = selection_list[index_number]



def game_with_computer(player_01_name,gesture_selection):
        Game_02 = set_computer_game(player_01_name,gesture_selection)

        for win_combination in Game_02.win_combination:
                if [gesture_selection,computer_2.gesture_selection] == win_combination:
                        return player_01_name
                elif [computer_2.gesture_selection, gesture_selection] == win_combination:
                        return computer_2.name







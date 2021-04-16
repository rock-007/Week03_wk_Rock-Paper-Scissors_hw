from flask import render_template, request
from app import app
from models.playing_game import *


@app.route ('/')
def index():
    str_arg = "Please insert the player_01 and Player_02 gesture selection in the URL"

    return render_template("index.html", result=str_arg, winner=False)


@app.route ('/<player_1_selection>/<player_2_selection>')
def playing_game(player_1_selection, player_2_selection):
    print(player_1_selection)

    result = play_game(player_1_selection,player_2_selection)
    print(result)

    return render_template("index.html", result=result, winner= True )


@app.route('/play', methods=["GET","POST"])
def playing_with_computer():

    winner_name = None
    if request.method =="POST":
        print(request.form['player_01_name'])
        print(request.form['gesture_selection'])
        winner_name = game_with_computer(request.form['player_01_name'],request.form['gesture_selection'])
        print(winner_name)
        print("winner_name")

    return render_template("computer.html", winner_name=winner_name)



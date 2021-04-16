from flask import render_template
from app import app
from models.playing_game import *


@app.route ('/')
def index():
    


    return render_template("index.html")


@app.route ('/<player_1_selection>/<player_2_selection>')
def playing_game(player_1_selection, player_2_selection):
    print(player_1_selection)

    result = play_game(player_1_selection,player_2_selection)
    print(result)

    return render_template("index.html", result=result )



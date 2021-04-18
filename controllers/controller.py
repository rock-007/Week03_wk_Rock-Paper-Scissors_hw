from flask import render_template, request, redirect, url_for
from app import app
from models.playing_game import *


@app.route ('/')
def index():
    str_arg = "Please insert the player_01 and Player_02 gesture selection in the URL"

    return render_template("index.html", result=str_arg, winner=False)


@app.route ('/<player_1_selection>/<player_2_selection>')
def playing_game(player_1_selection, player_2_selection):


    return redirect(url_for('result', value_1=player_1_selection, value_2=player_2_selection ))


@app.route('/result/<value_1>/<value_2>')
def result(value_1, value_2):

    winner_name = play_game(value_1, value_2) 

    return render_template("index.html",player_1= player_1,value_1=value_1, player_2= player_2,value_2= value_2, winner_name=winner_name, winner= True )


@app.route('/play', methods=["GET","POST"])
def playing_with_computer():

    winner_name = None
    if request.method =="POST":
        player_name = request.form['player_01_name']
        player_selection = request.form['gesture_selection']
        winner_name = game_with_computer(player_name, player_selection)
    else:
        player_name= None
        player_selection= None 



    return render_template("computer.html",player_name= player_name,player_selection=player_selection, computer_selection= computer_2.gesture_selection, winner_name=winner_name)



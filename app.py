from flask import Flask, request
import random
import json
from constants import SUITS, NO_GAME, PRE_GAME, IN_GAME

app = Flask(__name__, static_url_path='')

players = []
deck = []
discard_pile = []
game_status = NO_GAME
game_code = ""


def split(arr, number):
    return (arr[:number], arr[number:])

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/status')
def status():
    global game_status
    return game_status

def shuffle_deck():
    global deck
    num_cards = len(deck)
    for i in range(num_cards):
        next_card = random.randrange(i, num_cards)
        temp = deck[i]
        deck[i] = deck[next_card]
        deck[next_card] = temp

def instantiate_deck():
    global deck
    global discard_pile
    deck = []
    discard_pile = []
    for s in SUITS:
        for i in range(13):
            deck.append((s, i + 1))
    deck.append(('J', 0))
    deck.append(('J', 0))


@app.route('/new_game', methods = ['POST'])
def new_game():
    args = request.get_json()
    global game_status
    if game_status == NO_GAME:
        instantiate_deck()
        shuffle_deck()
        global players
        print(args["name"])
        players = [args["name"]]
        global game_code
        game_code = args["gid"]
        game_status = PRE_GAME
        return "0"
    return "1"

@app.route('/join_game', methods = ['POST'])
def join_game():
    global players
    global game_status
    if len(players) > 5 or game_status != PRE_GAME: # max number of players is 6
        return "1"
    user_name = request.get_json()["name"]
    players.append(user_name)
    print(players)
    return "0"
    


@app.route('/pick_cards')
def pick_cards():
    num_cards = request.args.get('num_cards')
    global deck
    (cards, deck) = split(deck, num_cards)
    return json.dumps(cards)

#instantiate_deck()
#shuffle_deck()
#print(deck)
#print(json.dumps(deck[:5]))

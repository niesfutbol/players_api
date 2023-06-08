from fastapi import FastAPI
import json
import players_from_as as pfa


f = open("./players.json")
players = json.load(f)
PLAYERS = pfa.get_player_info_from_list(players["response"])

app = FastAPI()


@app.get("/player/{player_id}")
def get_player(player_id: int):
    return PLAYERS[player_id]


@app.get("/players")
def get_player():
    return pfa.get_player_and_id(players["response"])

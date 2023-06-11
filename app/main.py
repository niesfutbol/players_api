from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import players_from_as as pfa


f = open("./players.json")
players = json.load(f)
PLAYERS = pfa.get_player_info_from_list(players["response"])
headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}

app = FastAPI()


@app.get("/v1")
def get_player(player: int = 54):
    return JSONResponse(content=PLAYERS[player], headers=headers)


@app.get("/v1/players")
def get_player():
    return JSONResponse(content=pfa.get_player_and_id(players["response"], headers=headers))

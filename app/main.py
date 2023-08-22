from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import pandas as pd
import players_from_as as pfa


f = open("./data/players.json")
large = pd.read_csv("./data/larga_player.csv")
longer = pd.read_csv("./data/longer_player_table_23.csv")
players = json.load(f)
PLAYERS = pfa.get_player_info_from_list(players["response"])
headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}

app = FastAPI()


@app.get("/v1")
def get_player(player: int = 54):
    return JSONResponse(content=PLAYERS[player], headers=headers)


@app.get("/v1/players")
def get_player():
    return JSONResponse(content=pfa.get_player_and_id(players["response"]), headers=headers)


@app.get("/v1/percentile")
def get_player():
    return JSONResponse(content=large.to_dict(orient="records"), headers=headers)


@app.get("/v1/percentile_with_league_id")
def get_percentils_with_league_id():
    return JSONResponse(content=longer.to_dict(orient="records"), headers=headers)

import chess.pgn
import pandas as pd
import datetime

pgn = open("/Users/wel51x/Downloads/ficsgamesdb_201902_chess_nomovetimes_63077.pgn")
'''
game = chess.pgn.read_game(pgn)

print(game.headers)
print(type(game.headers))

headers = chess.pgn.read_headers(pgn)
print(headers)
print(type(headers))
'''
ix = 0
df_cols = ["Result", "BlackElo", "WhiteElo", "cat"]
Result = []
BlackElo = []
WhiteElo = []
my_df  = pd.DataFrame(columns = df_cols)
print("00000", datetime.datetime.now())
while True:
    game = chess.pgn.read_game(pgn)
    Result += [game.headers["Result"]]
    if Result[ix] == "1-0":
#        Result[ix] = 1
        Result[ix] = "White Win"
    elif Result[ix] == "0-1":
#        Result[ix] = -1
        Result[ix] = "Black Win"
    else:
#        Result[ix] = 0
        Result[ix] = "Draw"
    BlackElo += [game.headers["BlackElo"]]
    BlackElo[ix] = int(BlackElo[ix])
    WhiteElo += [game.headers["WhiteElo"]]
    WhiteElo[ix] = int(WhiteElo[ix])

    ix += 1
    if ix % 10000 == 0:
        print(ix, datetime.datetime.now())
    if ix % 1000 == 0:
        break
#print(Result, '\n', BlackElo, '\n', WhiteElo, '\n', )
my_df["Result"] = Result
my_df["BlackElo"] = BlackElo
my_df["WhiteElo"] = WhiteElo
my_df["diff"] = my_df["BlackElo"] - my_df["WhiteElo"]

print(my_df)
my_df.to_csv('my_df3.csv')

import chess.pgn
import pandas as pd
import datetime
import numpy as np

def categorize(score):
    bin = score - 700
    if bin < 0:
        bin = 0
    return int(bin / 100)

pgn = open("/Users/wel51x/Downloads/ficsgamesdb_201902_chess_nomovetimes_63077.pgn")

ix = 0
df_cols = ["Result", "Category"]
playerSet = {}
Result = []
categ = np.zeros(26)
print("00000", datetime.datetime.now())
while True:
    game = chess.pgn.read_game(pgn)
    '''
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
    '''

    ix += 1
    if ix % 10000 == 0:
        print(ix, datetime.datetime.now())
    if ix % 100000 == 0:
        break

    playerBlack = str([game.headers["Black"]])
    if playerBlack in playerSet.keys():
        continue
    else:
        playerSet[playerBlack] = 1
        BlackElo = [game.headers["BlackElo"]]
        BlackElo = int(BlackElo[0])
        categ[categorize(BlackElo)] += 1

    playerWhite = str([game.headers["White"]])
    if playerWhite in playerSet.keys():
        continue
    else:
        playerSet[playerWhite] = 1
        WhiteElo = [game.headers["WhiteElo"]]
        WhiteElo = int(WhiteElo[0])
        categ[categorize(WhiteElo)] += 1

#my_df["Result"] = Result
my_df  = pd.DataFrame(categ)
#my_df["Counts"] = categ

print(my_df)
print(len(playerSet))
my_df.to_csv('my_df4.csv')

import chess.pgn
import pandas as pd
import datetime

def categorize(diff):
    bin = 500 - diff
    if bin < 0:
        bin = 0
    elif bin > 1000:
        bin = 1000
    return str(int(bin / 50))

pgn = open("/Users/wel51x/Downloads/ficsgamesdb_201902_chess_nomovetimes_63077.pgn")

ix = 0
df_cols = ["Result", "Category"]
Result = []
categ = []
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
    BlackElo = [game.headers["BlackElo"]]
    BlackElo = int(BlackElo[0])
    WhiteElo = [game.headers["WhiteElo"]]
    WhiteElo = int(WhiteElo[0])
    categ += [categorize(BlackElo - WhiteElo)]
    categ[ix] = int(categ[ix])

    ix += 1
    if ix % 10000 == 0:
        print(ix, datetime.datetime.now())
    if ix % 100000 == 0:
        break

my_df["Result"] = Result
my_df["Category"] = categ

print(my_df)
my_df.to_csv('my_df2.csv')

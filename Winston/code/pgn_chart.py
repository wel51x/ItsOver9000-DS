import chess.pgn
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

def categorize(score):
    bin = score - 700
    if bin < 0:
        bin = 0
    if bin > 2000:
        bin = 2000
    return int(bin / 100)

pgn = open("/Users/wel51x/Downloads/ficsgamesdb_201902_chess_nomovetimes_63077.pgn")

ix = 0
df_cols = ["Result", "Category"]
playerSet = {}
Result = []
categ = np.zeros(21)
print("00000", datetime.datetime.now())
while True:
    game = chess.pgn.read_game(pgn)

    ix += 1
    if ix % 10000 == 0:
        print(ix, datetime.datetime.now())
    if ix % 490000 == 0:
        break

    playerBlack = str([game.headers["Black"]])
    BlackElo = [game.headers["BlackElo"]]
    BlackElo = int(BlackElo[0])
    if playerBlack in playerSet.keys():
        if playerSet[playerBlack] == BlackElo:
            continue
    else:
        playerSet[playerBlack] = BlackElo
        categ[categorize(BlackElo)] += 1

    playerWhite = str([game.headers["White"]])
    WhiteElo = [game.headers["WhiteElo"]]
    WhiteElo = int(WhiteElo[0])
    if playerWhite in playerSet.keys():
        if playerSet[playerWhite] == WhiteElo:
            continue
    else:
        playerSet[playerWhite] = WhiteElo
        categ[categorize(WhiteElo)] += 1

my_df  = pd.DataFrame(categ)
rang = list(range(800, 2801, 100))
ix = 0
for i in rang:
    rang[ix] = str(rang[ix])
    ix += 1
my_df["rang"] = rang
my_df.set_index([rang], inplace=True)
#print(my_df)
my_df.drop("rang", axis=1, inplace=True)

print(my_df)
print(len(playerSet))
my_df.to_csv('my_df4.csv')
ax = my_df.plot(kind='bar',legend=None, title="Distribution of Player Ratings")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Players")
plt.show()

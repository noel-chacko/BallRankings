import pandas as pd
import numpy as np
def ranker():
    rankings = pd.read_csv("nameCorrected.csv")
    rank = rankings.to_dict()
    espn = rank["ESPN"]
    on3 = rank["On3"]
    two47 = rank["24/7"]
    rivals = rank["Rivals"]
    all = pd.concat([rankings['ESPN'],rankings['On3'],rankings['24/7'],rankings['Rivals']]).unique()
    compiled = {}
    for a,x in espn.items():
        for b,y in on3.items():
            for c,w in two47.items():
                for d,z in rivals.items():
                    for player in all:
                        if x == y == w == z == player:
                            compiled[player] = ((a+b+c+d)/4)

    rank_list = list(compiled)
    agg_ranks = pd.DataFrame(rank_list, columns=["Player"])
    agg_ranks.to_csv('rankings.csv',index=False)
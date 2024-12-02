import pandas as pd
import numpy as np

def get_distance(point1, point2):
    return abs(point1 - point2)

df_ = pd.read_excel("/Users/aidapendasfernandez/Documents/GitHub/aidapendas/adventOfCode2024/Day1/Lists.xlsx")

list1 = df_["List1"].tolist()
list1.sort()
list2 = df_["List2"].tolist()
list2.sort()

distances = [get_distance(p1, p2) for p1, p2 in zip(list1, list2)]

print(f"Sum of distances between the two lists: {np.sum(distances)}")

similarity_score_list = [num * list2.count(num) for num in list1]

print(f"Similarity score between the two lists: {np.sum(similarity_score_list)}")


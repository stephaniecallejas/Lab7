# Coded by Stephanie Callejas
# Last Edit: 5 Dec 2018
# CS2302 Lab 7 Project
# Instructors: Diego Aguirre and Saha, Manoj Pravakar
# Goal: Implement edit distance algorithm


def edit_distance(s1, s2):
    m = len(s1)+1
    n = len(s2)+1

    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i, j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i, j]


print(edit_distance("Helloworld", "HalloWorld"))

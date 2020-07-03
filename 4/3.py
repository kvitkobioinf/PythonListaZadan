import os

if __name__ == "__main__":
    with open(os.path.abspath("./data/football.csv"), 'r') as f:
        data = [row.split(",") for row in f.read().splitlines()]
        
    g_index = data[0].index("Goals")
    ga_index = data[0].index("Goals Allowed")

    highest = [-1, -1]
    for i in range(1, len(data)):
        calc = int(data[i][g_index]) - int(data[i][ga_index])
        if highest[1] < calc:
            highest[0] = i
            highest[1] = calc

    print(data[highest[0]][0], "with", highest[1], "goals")
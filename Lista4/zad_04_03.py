import os

if __name__ == "__main__":
    with open(os.path.abspath("football.csv"), 'r') as f:
        data = [row.split(",") for row in f.read().splitlines()]
        
    g_index = data[0].index("Goals")
    ga_index = data[0].index("Goals Allowed")

    highest = [9999, 9999]
    for i in range(1, len(data)):
        calc = abs(int(data[i][g_index]) - int(data[i][ga_index]))
        #print(str(data[i][0]) + " - " + str(calc))
        if highest[1] > calc:
            highest[0] = i
            highest[1] = calc

    print("Najmniejsza różnica w golach strzelonych przeciwnikom i przez przeciwników (" + str(highest[1]) + ") uzyskał " + str(data[highest[0]][0]))
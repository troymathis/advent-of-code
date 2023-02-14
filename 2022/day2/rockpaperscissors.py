games = ""
with open('demo_input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        games += line

def splitInputs(games):
    list = games.split("\n")
    appendedList = []
    for game in list:
        appendedList.append(game.split(" "))
    return appendedList

def pickScore(appendedList):
    for x in range(len(appendedList)):
        for y in range(2):
            if appendedList[x][y] == "A":
                appendedList[x][y] = 1
            elif appendedList[x][y] == "B":
                appendedList[x][y] = 2
            elif appendedList[x][y] == "C":
                appendedList[x][y] = 3
            elif appendedList[x][y] == "X":
                appendedList[x][y] = 1
            elif appendedList[x][y] == "Y":
                appendedList[x][y] = 2
            elif appendedList[x][y] == "Z":
                appendedList[x][y] = 3
    return appendedList

def compare(appendedList):
    for x in range(len(appendedList)):
        if appendedList[x][0] == appendedList[x][1]:
            appendedList[x][1] += 3
        elif appendedList[x][0] > appendedList[x][1]:
            appendedList[x][1] += 0
        elif appendedList[x][0] < appendedList[x][1]:
            appendedList[x][1] += 6
    return appendedList

scores = compare(pickScore(splitInputs(games)))

for x in range(len(scores)):
    print(scores[x][1])
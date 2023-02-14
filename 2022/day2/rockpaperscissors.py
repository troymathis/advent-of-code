games = ""
with open('input.txt', 'r') as f:
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
            # draw condition
        if appendedList[x][0] == appendedList[x][1]:
            appendedList[x][1] += 3
            # lose conditions
        elif (appendedList[x][0] == 2 and appendedList[x][1] == 1) or (appendedList[x][0] == 1 and appendedList[x][1] == 3) or (appendedList[x][0] == 3 and appendedList[x][1] == 2):
            appendedList[x][1] += 0
            # win conditions
        elif (appendedList[x][0] == 1 and appendedList[x][1] == 2) or (appendedList[x][0] == 3 and appendedList[x][1] == 1) or (appendedList[x][0] == 2 and appendedList[x][1] == 3):
            appendedList[x][1] += 6
    return appendedList

def partTwo(appendedList):
    for x in range(len(appendedList)):
        if appendedList[x][1] == 1:
            if appendedList[x][0] == 1:
                appendedList[x][1] = 3
            if appendedList[x][0] == 2:
                appendedList[x][1] = 1
            if appendedList[x][0] == 3:
                appendedList[x][1] = 2
        elif appendedList[x][1] == 2:
            if appendedList[x][0] == 1:
                appendedList[x][1] = 4
            if appendedList[x][0] == 2:
                appendedList[x][1] = 5
            if appendedList[x][0] == 3:
                appendedList[x][1] = 6
        elif appendedList[x][1] == 3:
            if appendedList[x][0] == 1:
                appendedList[x][1] = 8
            if appendedList[x][0] == 2:
                appendedList[x][1] = 9
            if appendedList[x][0] == 3:
                appendedList[x][1] = 7
    return appendedList

scores = partTwo(pickScore(splitInputs(games)))

total = 0
for x in range(len(scores)):
    total += scores[x][1]

print(total)
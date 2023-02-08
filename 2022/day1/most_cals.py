elves1 = ""
with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        elves1 += line

def mostCals(elves):
    elves = elves.split("\n\n")
    Sum = 0
    for i in range(len(elves)):
        elves[i] = elves[i].split("\n")
        for j in range(len(elves[i])):
            elves[i][j] = int(elves[i][j])
        if sum(elves[i]) > Sum:
            Sum = sum(elves[i])
    

    return Sum

print(mostCals(elves1))
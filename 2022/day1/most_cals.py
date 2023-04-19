elves1 = ""
with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        elves1 += line
         
def mostCals(elves):
    elves = elves.split("\n\n")
    Sums = []
    for i in range(len(elves)):
        elves[i] = elves[i].split("\n")
        for j in range(len(elves[i])):
            elves[i][j] = int(elves[i][j])
        Sums.append(sum(elves[i]))
    Sums.sort()
    return Sums[-1]+Sums[-2]+Sums[-3]

print(mostCals(elves1))
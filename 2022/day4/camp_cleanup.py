pairs = ""
with open('demo_input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        pairs += line

def splitPairs(pairs):
    newPairs = pairs.split("\n")
    draft_pairs = []
    for i in range(len(newPairs)):
        draft_pairs.append(newPairs[i].split(","))
    return draft_pairs

ranges_final = []
def findContainers(splitPairs):
    for i in range(len(splitPairs)):
        ranges = []
        ranges2 = []
        boundary1_2 = int(splitPairs[i][1][0])
        boundary2_2 = int(splitPairs[i][1][2])
        boundary2 = int(splitPairs[i][0][2])
        boundary1 = int(splitPairs[i][0][0])
        integer = 0
        integer2 = 0
        while integer < (boundary2-boundary1+1):
            ranges.append(boundary1+integer)
            integer += 1
        while integer2 < (boundary2_2 - boundary1_2+1):
            ranges2.append(boundary1_2+integer2)
            integer2 +=1
        ranges_final.append([ranges, ranges2])
    return ranges_final

print(findContainers(splitPairs(pairs)))
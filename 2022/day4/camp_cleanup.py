

pairs = ""
with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        pairs += line


def splitPairs(pairs):
    newPairs = pairs.split("\n")
    draft_pairs = []
    draft_pairsv2 = []
    for i in range(len(newPairs)):
        draft_pairs.append(newPairs[i].split(","))
    for j in range(len(draft_pairs)):
        draft_pairsv2.append(
            [draft_pairs[j][0].split("-"), draft_pairs[j][1].split("-")]
        )
    return draft_pairsv2


ranges_final = []


def findContainers(splitPairs):
    for i in range(len(splitPairs)):
        ranges = []
        ranges2 = []
        boundary1_2 = int(splitPairs[i][1][0])
        boundary2_2 = int(splitPairs[i][1][1])
        boundary2 = int(splitPairs[i][0][1])
        boundary1 = int(splitPairs[i][0][0])
        integer = 0
        integer2 = 0
        while integer < (boundary2 - boundary1 + 1):
            ranges.append(boundary1 + integer)
            integer += 1
        while integer2 < (boundary2_2 - boundary1_2 + 1):
            ranges2.append(boundary1_2 + integer2)
            integer2 += 1
        ranges_final.append([ranges, ranges2])
    return ranges_final


def fullyContain(ranges):
    count = 0
    for i in range(len(ranges)):
        stretch1 = ranges[i][0]
        stretch2 = ranges[i][1]
        if set(stretch1) >= set(stretch2):
            count += 1
        elif set(stretch1) <= set(stretch2):
            count += 1
    return count

def overlap(ranges):
    count = 0
    for i in range(len(ranges)):
        stretch1 = ranges[i][0]
        stretch2 = ranges[i][1]
        if list(set(stretch1) & set(stretch2)):
            count +=1
    return count

print(overlap(findContainers(splitPairs(pairs))))

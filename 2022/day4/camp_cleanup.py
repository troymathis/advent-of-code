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

print(splitPairs(pairs))
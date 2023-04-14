runsacks= ""
with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        runsacks += line

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_dict = {letter:idx+1 for idx, letter in enumerate(alphabet)}

def splitRunSacks(runsacks):
    runsacks = runsacks.split("\n")
    return runsacks

elvesSep = splitRunSacks(runsacks)
finalSplit = []

def splitCompartments(runsacks):
    for i in range(len(elvesSep)):
        length = len(elvesSep[i])
        string = elvesSep[i]
        finalSplit.append([string[:len(string)//2],string[len(string)//2:]])
    return finalSplit
matchReady = splitCompartments(elvesSep)
matches = []

def findMatch(matchReady):
    for i in range(len(matchReady)):
        for first in matchReady[i][0]:
            for second in matchReady[i][1]:
                  match_found = False
                  if first == second:
                      matches.append(first)
                      match_found = True
                      break
            if match_found:
                      break
    numbers = [alphabet_dict[char] for char in matches if char in alphabet_dict]
    return numbers

def total(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(total(findMatch(matchReady)))
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

number_of_crates = len(lines[0])//4
crate_lines = lines[:lines.index('\n')-1]
moving_lines = lines[lines.index('\n')+1:]

def makeStacks():
    obj = [[] for i in range(number_of_crates)]
    for cratelines in crate_lines:
        print(cratelines)
        for i in range(1, len(cratelines), 4):
            if cratelines[i].isspace() == False:
                obj[i//4].append(cratelines[i])
    print(obj)
    return obj


def moveCrates(moving_lines, obj):
    moving_values = []
    for ml in moving_lines:
        res = re.findall('\d+', ml)
        moving_values.append(res)
    print(moving_values)
    for j in range(len(moving_values)):
        how_many = int(moving_values[j][0])
        from_where = int(moving_values[j][1]) - 1
        to_where = int(moving_values[j][2]) - 1
        temp = obj[from_where][0:how_many]
        temp.reverse()
        for k in range(len(temp)):
            obj[from_where].remove(temp[k])
        for k in range(len(temp)):
            obj[to_where].insert(0, temp[k])
    top = ''
    for i in obj:
        top += i[0]
    return top



print(moveCrates(moving_lines, makeStacks()))
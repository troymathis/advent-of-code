with open('demo_input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

number_of_crates = len(lines[0])//4
crate_lines = lines[:lines.index('\n')-1]
moving_lines = lines[lines.index('\n')+1:]

def makeStacks(stacks):
    obj = [[] for i in range(number_of_crates)]
    for cratelines in crate_lines:
        print(cratelines)
        for i in range(1, len(cratelines), 4):
            obj[i//4].append(cratelines[i])
    return obj

print(makeStacks(crate_lines))
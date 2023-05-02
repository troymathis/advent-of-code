stacks = ""
with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        stacks += line

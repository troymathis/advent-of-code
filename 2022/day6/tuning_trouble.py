data_stream = ""
with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        data_stream += line

new = list(data_stream)

def findSub(new):
    length = len(new)
    for i in range(0, length-3):
        sub = new[i:i+4]
        if len(sub) == len(set(sub)):
            return i+4

print(findSub(new))
data_stream = ""
with open("demo_input.txt", "r") as f:
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
        print(sub)

print(findSub(new))
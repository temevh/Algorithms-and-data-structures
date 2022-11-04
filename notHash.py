import time


arr = []

file = open("hashText.txt", "r")
for line in file:
    arr.append(line.strip())

st = time.time()
print(arr.index("lazzarone"))
et = time.time()

print("Execution time", et-st, "seconds")

import time


def readFile():
    file = open("words_alpha.txt", "r", encoding="utf-8")
    arr = []
    for line in file:
        arr.append(line.strip())
    return arr


def compare(allwords):
    matches = 0
    file = open("kaikkisanat.txt", "r", encoding="utf-8")
    for line in file:
        if line.strip() in allwords:
            matches += 1

    print("Matching words:", matches)


def writeToFile(add, comp, runtime_total):
    file = open("compareRuntimeList.txt", "a", encoding="utf-8")
    file.write("ACTION       |   RUNTIME(s)\n")
    file.write("-------------|----------------\n")
    file.write("Add to table |"+str("%.8f" % add)+"\n")
    file.write("Compare      |"+str("%.8f" % comp)+"\n")
    file.write("-------------|----------------\n")
    file.write("Total runtime: "+str("%.8f" % runtime_total))


runtime_total = 0
st = time.time()
allwords = readFile()
et = time.time()
add = et-st
st = time.time()
compare(allwords)
et = time.time()
comp = et-st
runtime_total += (add+comp)
print("ACTION       |   RUNTIME(s)")
print("-------------|----------------")
print("Add to table |", "%.8f" % add)
print("Compare      |", "%.8f" % comp)
print("-------------|----------------")
print("Total runtime: ", "%.8f" % runtime_total)
writeToFile(add, comp, runtime_total)

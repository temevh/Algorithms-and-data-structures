class HashLinear:
    def __init__(self, M):
        self.M = M             
        self.T = [None] * M

    def insert(self, data):
        i = HashLinear.hasher(data, self.M)
        while(True):
            if self.T[i] == None:
                self.T[i] = data
                break
            else:
                if self.T[i] == data:
                    break
                else:
                    if i == len(self.T)-1:
                        i = 0
                    else:
                        i += 1
        return

    def hasher(Sel, selM):
        sum = 0
        i = 0
        for i in range(len(Sel)):
            sum += int(ord(Sel[i]))
        return sum % selM

    def print(self):
        ar = []
        for x in self.T:
            if x != None and x != -1:
                ar.append(x)
        print(*ar, sep=' ')


    def delete(self, data):
        i = HashLinear.hasher(data, self.M)
        while(True):
            if self.T[i] == None:
                break
            else:
                if self.T[i] == data:
                    self.T[i] = -1
                    break
                else:
                    if i == len(self.T)-1:
                        i = 0
                    else:
                        i += 1
        return

    

if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1
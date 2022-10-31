lista = [4,1,51,7,125,4,1,5,4,4,4,16,159569,15,5124,731,51,125,16,4,1]

listarem = []
for i in lista:
    if i not in listarem:
        listarem.append(i)

print(listarem)
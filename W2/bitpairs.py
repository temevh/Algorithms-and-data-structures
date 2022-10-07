#basis/basics for the function from https://www.geeksforgeeks.org/sum-of-all-etaisyyss-between-occurrences-of-same-characters-in-a-given-string/

def pairs(s):
    tavattu = [0 for i in range(256)]
    etaisyys = [0 for i in range(256)]

    for i in range(256):
        tavattu[i] = 0
        etaisyys[i] = 0
    
    summa = 0

    for i in range (len(s)):
        if s[i]=="1":
            summa += tavattu[ord(s[i])] * i - etaisyys[ord(s[i])]
            tavattu[ord(s[i])] += 1
            etaisyys[ord(s[i])] += i;
 
    return(summa)

if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71


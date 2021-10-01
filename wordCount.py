import time
import pymp
import re

def main():

    with open("shakespeare1.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file1 = []
    for line in Lines:
        file1.append(re.split(' ',line))
    """
    with open("shakespeare2.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file2 = []
    for line in Lines:
        file2.append(re.split(re.split(' ',line))

    with open("shakespeare3.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file3 = []
    for line in Lines:
        file3.append(re.split(' ',line))

    with open("shakespeare4.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file4 = []
    for line in Lines:
        file4.append(re.split(' ',line))

    with open("shakespeare5.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file5 = []
    for line in Lines:
        file5.append(re.split(' ',line))

    with open("shakespeare6.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file6 = []
    for line in Lines:
        file6.append(re.split(' ',line))

    with open("shakespeare7.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file7 = []
    for line in Lines:
        file7.append(re.split(' ',line))

    with open("shakespeare8.txt",'r',encoding = 'utf8',errors='ignore') as f:
        Lines = [ lines.rstrip('\n') for lines in f]
    file8 = []
    for line in Lines:
        file8.append(re.split(' ',line))
    """
    listRet = pymp.shared.list()
    wordList = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    listWords = pymp.shared.list(wordList)
    listRet.append(file1)
    dictRet = pymp.shared.dict()
    for val in wordList:
        dictRet[val]=0
    print(dictRet)
    with pymp.Parallel() as p:
        sumLock = p.lock
        for item in listWords:
            sumLock.acquire()
            for val in p.iterate(listRet):

                if(val is item):
                    dictRet[item]+=1
            sumLock.release()
    print(dictRet)
    """
    listRet.append(file2)
    listRet.append(file3)
    listRet.append(file4)
    listRet.append(file5)
    listRet.append(file6)
    listRet.append(file7)
    listRet.append(file8)
    """


if __name__ == "__main__":
    main()

#GTex=open(input("file?")).readline().rstrip()
k=int(input("k-mer?"))
t=int(input("How many times do you want it to appear within the interval, L?"))
count={}
GTex="CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"

def FindClumps(Text,k,t):
    n = len(GTex)
    start=0
    for x in range(n-k+1):
        if GTex[start:k] in count:
            count[GTex[start:k]]=count[GTex[start:k]]+1
        else:
            count[GTex[start:k]] = 1
        start+=1
        k+=1
    if "" in count:
        del count[""]
    counter=0
    for k,v in count.items():
        if v>=t:
            print(k,v)
            counter+=1
            print(counter)

#the only difference between this and finding frequent genome is that it
#looks for a certain amount of repetitions




FindClumps(GTex,k,t)






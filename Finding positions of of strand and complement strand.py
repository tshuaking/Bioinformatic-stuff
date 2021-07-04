filename=input("filename?")
Genome=open(filename).readline().rstrip()
Pattern=input("Pattern?")
def patternfinder(Pattern,Genome):
    revpat=Pattern[::-1]  #reversing the pattern for easier analysis
    revcomp="" #variable with empty space to store values later
    jump=len(Pattern) #the length of the pattern
    lstn=list()

    for num in range(len(Pattern)): #revpat and Pattern are the same length
        if revpat[num]=="A":revcomp+"T"   #checking the reverse pattern to replace it with complement base
        elif revpat[num] == "T": revcomp + "A"
        elif revpat[num] == "C": revcomp + "G"
        elif revpat[num] == "G": revcomp + "C"

    for number in range(len(Genome)):
        if Genome[number:number+jump]== Pattern:lstn.append(number)
        #number is the starting position and "number+jump" is the boundary of the pattern to check
        if Genome[number:number+jump]== revcomp:lstnappend(number)
    print(" ".join(str(x) for x in lstn)) #convert integers to str to be able to use .join()
patternfinder(Pattern,Genome)
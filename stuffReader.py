import cPickle
def stuffGetter(path):
    #A function that loads files, so I don't have to type as much.
    return cPickle.load(open(path, "rb"))

def limit(gene, listOfSpecies):
    #Creates a small matrix called outputDict, whch is ratioDict, except limited to only a few species
    outputDict = {}
    ratioDict = stuffGetter("finalData/"+gene.lower().capitalize())
    for g in ratioDict:
        if g in listOfSpecies:
            outputDict[g] = {}
            for j in ratioDict[g]:
                if j in listOfSpecies:
                    outputDict[g][j] = ratioDict[g][j]
    return outputDict

#Coming soon!
#def average(gene):
#    ratioDict = stuffGetter("finalData/"+gene.lower().capitalize())
#    addedNums = [float(0) , 0]
#    for i in ratioDict:
#        for g in ratioDict[i]:
#            print ratioDict[i][g]
#            addedNums[0] = addedNums[0] + ratioDict[i][g]
#            addedNums = addedNums[0] + 1
#    return addedNums
#print limit("SIX6", ["rheMac3", "otoGar3", "chlSab2"])
print average("pax6")

import cPickle
def stuffGetter(path):
    #A function that loads files, so I don't have to type as much.
    return cPickle.load(open(path, "rb"))

def limit(gene, listOfSpecies):
    #Creates a small matrix called outputDict, whch is ratioDict, except limited to only a few species
    outputDict = {}
    ratioDict = stuffGetter("finalData/"+gene.upper())
    for g in ratioDict:
        if g in listOfSpecies:
            outputDict[g] = {}
            for j in ratioDict[g]:
                if j in listOfSpecies:
                    outputDict[g][j] = ratioDict[g][j]
    return outputDict

def numberFilter(gene, listOfSpecies=[]):
    pass
def average(gene):
    ratioDict = stuffGetter("finalData/"+gene.upper())
    addedNum = 0.0
    timesAdded = 0
    for i in ratioDict:
        for g in ratioDict[i]:
            addedNum = addedNum + ratioDict[i][g]
            timesAdded = timesAdded + 1
    return addedNum/timesAdded

def makeTable(matrix, file):
    f = open(file, "w")
    f.write("")
    top = ""
    keys = list(matrix.keys())
    keys.sort()
    f.write(",".join([ "Species" ] + keys) + "\n")
    for key in keys:
         f.write(",".join([ key ] + [ str(matrix[key][key2]) for key2 in keys ]) + "\n")
    f.close()

def autorun(listOfLists, geneList=["CRYGB", "OTX1", "PAX6", "PDE6B", "SIX6", "TULP1", "VSX2"]):
    for i in listOfLists:
        for g in geneList:
            print g
            print limit(g,i)


#print limit("six6", ["rheMac3", "falChe1", "petMar2"])
#print average("six6")
geneList = ["CRYGB", "OTX1", "PAX6", "PDE6B", "SIX6", "TULP1", "VSX2"]
treeDict = {"Blue":["rheMac3", "chlSab2", "otoGar3"], "Red":["speTri2", "jacJac1", "mesAur1"], "Brown":["hetGla2", "chiLan1", "ochPri3"],"Green":["felCat8", "canFam3", "eptFus1"], "Orange":["eleEdw1", "chrAsi1", "echTel2"], "Pink":["rheMac3", "falChe1", "anaPla1"]}

for o in geneList:
    for i in treeDict:
        makeTable(limit(o,treeDict[i]), "tables/" + o + "/"+i+".csv")
#makeTable(stuffGetter("finalData/Pax6"), "pax6General.csv")
#print limit("CRYGB", ["rheMac3", "jacJac1", "felCat8"])

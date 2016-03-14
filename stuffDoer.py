import cPickle
import re
def stuffGetter(path):
    return cPickle.load(open(path, "rb"))
def stuffDoer(diffs,sames, gene):
    ratios = stuffGetter("data/emptyMatrix")
    for i in diffs:
        for g in diffs[i]:
            try:
                ratios[i][g] = float(diffs[i][g])/(float(sames[i][g]) + diffs[i][g])
            except:
                ratios[i][g] = float(0)
    def fileWriter(path, data):
        cPickle.dump(data, open(path, "wb"))
    fileWriter("finalData/" + gene.upper(), ratios)
    return ratios
gene = raw_input("What is your gene")
geneList = ["CRYGB", "OTX1", "PAX6", "PDE6B", "SIX6", "TULP1", "VSX2"]
if gene == "Easter egg":
    print "You found me. This feature was created to help mrtopsyt, and probably will be useless if you don't have these genes: \n" + str(geneList)
    for i in geneList:
        stuffDoer(stuffGetter("data/" + i + "diffs"), stuffGetter("data/" + "sames"), i)
        print "Thanks. Here is VSX2's alignment " + str(cPickle.load(open("finalData/" + "Otx1".capitalize().lower())))
else:
    stuffDoer(stuffGetter("data/" + gene.upper() + "diffs"), stuffGetter("data/" + gene.upper() + "sames"), gene)
    print cPickle.load(open("finalData/" + gene.capitalize().lower()))

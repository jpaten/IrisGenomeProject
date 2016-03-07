from fractions import Fraction
import cPickle
import re
def stuffGetter(path):
    return cPickle.load(open(path, "rb"))
diffs = stuffGetter('data/SIX6Diffs')
sames = stuffGetter("data/SIX6Sames")
ratios = stuffGetter("data/emptyMatrix")

for i in diffs:
    for g in diffs[i]:
       ratios[i][g] = float(diffs[i][g])/float(sames[i][g])
def fileWriter(path, data):
        cPickle.dump(data, open(path, "wb"))
fileWriter("finalData/SIX6", ratios)
print stuffGetter("finalData/SIX6")

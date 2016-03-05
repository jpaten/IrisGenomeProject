from fractions import Fraction
import cPickle
def stuffGetter(path):
    return cPickle.load(open(path, "rb"))
diffs = stuffGetter('data/pax6Diffs')
sames = stuffGetter("data/pax6Sames")
for i in diffs:
    for g in i:
        print diffs[i][g]

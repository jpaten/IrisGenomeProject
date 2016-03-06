from fractions import Fraction
import cPickle
def stuffGetter(path):
    return cPickle.load(open(path, "rb"))
diffs = stuffGetter('data/PAX6Diffs')
sames = stuffGetter("data/PAX6Sames")
ratios = {}
for i in diffs:
    for g in diffs[i]:
        try:
            print "yay"
            ratios[i][g] = float(diffs[i][g])/float(sames[i][g])
        except:
            print "boo"
            continue
print ratios

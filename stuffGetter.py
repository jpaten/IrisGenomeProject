#This program counts differences. This bit just imports things though.
import re
import sys
from Bio import AlignIO
import cPickle as pickle
a = 0
def getStuff(workAlignment, geneName):
        speciesList = []
        global speciesList
        def rmDot(string):
                #Removes dots
                return string.split(".")[0]
        def makeMatrix(species):
                #Makes the matrix that things can be stored in.
                stuffDict = {}
                for i in species:
                        stuffDict[i] = {}
                        for j in species:
                                stuffDict[i][j] = 0
                return stuffDict
        for i in AlignIO.parse(workAlignment, "maf"):
                #Creates a list of species to be used in a matrix.
                for q in xrange(len(str(i.get_column(0)))):
                        if rmDot(list(i)[q].id) not in speciesList:
                                speciesList.append(rmDot(list(i)[q].id))

        #runs the makeMatrix functionto create dictOfCOunts, which will hold all of the counts.
        dictOfCounts = makeMatrix(speciesList)
        dictOfSames = makeMatrix(speciesList)

        for i in AlignIO.parse(workAlignment, "maf"):
                #Loops through each block in the alignment.i is an Object that can be turned into a list or string and has several deprecated functions (which I use).
                columnDict = {}
                for j in xrange(i.get_alignment_length()):
                        #creates columnDict, a dictionary that contains a apecies name and a letter
                        global columnDict
                        column = i.get_column(j)
                        if '-' or "n" or "N" not in column:
                                y = 0
                                for k in column:
                                        columnDict[rmDot(list(i)[y].id)] = k
                                        y = y + 1
                        for g in columnDict:
                                #Populates dictOfCounts
                                for h in columnDict:
                                        if columnDict[h] != columnDict[g]:
                                                dictOfCounts[g][h]= dictOfCounts[g][h] + 1
                                        else:
                                                dictOfSames[g][h] = dictOfSames[g][h] + 1
        def fileWriter(path, data):
                pickle.dump(data, open(path, "wb"))
        fileWriter("data/" + geneName + "diffs", dictOfCounts)
        fileWriter("data/" + geneName + "sames", dictOfSames)
        fileWriter("data/emptyMatrix", makeMatrix(speciesList))
geneDict = {"PAX6Alignments":"PAX6", "OTX1Alignments.maf":"OTX1", "CRYGBAlignments":"CRYGB", "SIX6Alignments.maf.txt":"SIX6", "PDE6BAlignments":"PDE6B", "TULP1Alignments.maf.txt":"TULP1", "VSX2Alignments.maf":"VSX2"}
alignment = raw_input("What file is your alignment in? ")
if alignment == "Secret password":
    for z in geneDict:
        print "Autorun on a ton of things activated. If your Github username isn't mrtopsyt, you probably shouldn't be using this. If, however, you have all of these genes " + str(geneDict) + " go right ahead."
        getStuff(z, geneDict[z])
else:
    gene = raw_input("What gene are you running me on? ")
    getStuff(alignment, gene)


#print dictOfSames
#print dictOfCounts

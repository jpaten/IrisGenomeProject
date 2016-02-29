#This program counts differences. This bit just imports things though.
import re
import sys
from Bio import AlignIO
#speciesList is a list of all the species that are revelant to this project.
speciesList = []        
a = 0                

def rmDot(string):
        #Removes dots
        return re.findall("(.*)[.]",string)[0]
def makeMatrix(species):
        #Makes the matrix that things can be stored in.
        stuffDict = {}
        for i in species:
                stuffDict[i] = {}
                for j in species:
                        stuffDict[i][j] = 0
        return stuffDict
for i in AlignIO.parse("PAX6Alignments", "maf"):
                #Creates a list of species to be used in a matrix.
                for q in xrange(len(str(i.get_column(0)))):
                        if rmDot(list(i)[q].id) not in speciesList:
                                speciesList.append(rmDot(list(i)[q].id))

#runs the makeMatrix functionto create dictOfCOunts, which will hold all of the counts.
dictOfCounts = makeMatrix(speciesList)
dictOfSames = makeMatrix(speciesList)
                                
for i in AlignIO.parse("PAX6Alignments", "maf"):
        #Loops through each block in the alignment.i is an Object that can be turned into a list or string and has several deprecated functions (which I use).
        columnDict = {}
        for j in xrange(i.get_alignment_length()):
                #creates columnDict, a dictionary that contains a apecies name and a letter
                global columnDict
                column = i.get_column(j)
                if '-' or "n" not in column:
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
                                

print dictOfSames
print dictOfCounts

#This program reads sections of files in sections, if they are to big to read all at once
import sqlite3
import re
#This list contains all species I am looking for
speciesList = ["macMul", "chlSab",]
test = raw_input("Enter a file")
def reader(file, databaseOrNot):
    f = open(file)
    for i in f:
        print i
        raw_input()
    f.close()
#reader("upstream1000.knowngene.maf", False)

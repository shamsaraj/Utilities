import os
import fileinput
path = "G:/new/Ready"
for filename in os.listdir(path): 
    for line in fileinput.input(path + "/" + filename, inplace =1):
        line = line.replace ("0.000 Zn" , "2.000 Zn" )
	line = line.replace ("0.000 Ca" , "2.000 Ca" )
        print (line)

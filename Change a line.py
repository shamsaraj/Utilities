import os
import fileinput
path = "D:\Shamsara\Allr"
for filename in os.listdir(path): 
    for line in fileinput.input(path + "/" + filename, inplace =1):
        if line.startswith("D:"):
            L = len (filename)
            L = L - 5
            line = filename [ :L] 
        print (line)

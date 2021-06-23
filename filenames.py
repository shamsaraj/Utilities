import os
import fileinput
path = "E:/HTVS/"
for dirname in os.listdir(path):
    print dirname
    for filename in os.listdir(path + dirname + "/" ):
            if filename.endswith (".txt"):
                filename2= filename [:-4]
                print filename2
                #cmd = "rename " + path + dirname + "/" + filename + " " + path + dirname + "/" + filename2 + ".csv"
                #os.system (cmd)
                os.rename (path + dirname + "/" + filename, path + dirname + "/" + filename2 + ".csv")

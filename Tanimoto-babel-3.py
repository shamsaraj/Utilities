#assumptions 
#It is for d3 project
#all files are in the path- selected molecules are in separated mol2- the previously finded actives are in a single tab limite text file (.smi-can be generated by MS excel from a CHEMBL file)
#file shoud be executed in the dircetory of molecules
import os
path = "d:/1"
Z= os.listdir(path)
N= len (Z)
for n in range (0,N):
        if Z[n].endswith(".mol2"):
                for m in range (0,N):
                        if m>n and Z[m].endswith(".mol2"):
                                cmd1 = "babel " + Z[n] + " " + Z[m] + " -ofpt >> Tanimoto-Select.txt"
                                os.system(cmd1)
                        
                
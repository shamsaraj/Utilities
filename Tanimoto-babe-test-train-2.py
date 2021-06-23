#assumptions
#For test train comparison
import os
pathTE = "d:/inputs/pygm-test/activessp"
zTE= os.listdir(pathTE)
nTE= len (zTE)
pathTR= "d:/inputs/pygm-train/activessp"
zTR= os.listdir(pathTR)
nTR= len (zTR)
for n in range (0,nTE):
        if zTE[n].endswith(".mol2"):
                for m in range (0,nTR):
                        if zTR[m].endswith(".mol2"):
                                cmd1 = "babel " + pathTE+ "/" + zTE[n] + " " + pathTR + "/" + zTR[m] + " -ofpt >> Tanimoto-Test-Train-PYGM.txt"
                                print zTE[n] + " <-------> " + zTR[m] 
                                os.system(cmd1)
                        #elif Z[m].endswith(".smi"):
                                #cmd2 = "babel " + Z[n] + " " + Z[m] + " -ofpt >> Tanimoto-Chem.txt"
                                #os.system(cmd2)
                

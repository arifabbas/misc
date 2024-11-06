import os
import sys

#starting point

STARTING= os.curdir
#for file in files:
i=1

def list_dir_elements(CURDIR,i):
    print(">"*i,CURDIR)
    files= os.listdir(CURDIR)
    
    for file in files: 
            if os.path.isfile(CURDIR+"/"+file):
                print("-"*(i+1),file)
            
            elif os.path.isdir(CURDIR+"/"+file):
                list_dir_elements(os.path.abspath(CURDIR+"/"+file),i=i+1)
            
            else:
                break

list_dir_elements(STARTING,1)

#
'''
-Desktop
--file1
--file2
--Dir1
---file1
---file2

'''
#

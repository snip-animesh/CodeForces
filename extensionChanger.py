import os
path=os.getcwd()
filenames=os.listdir(path)

for i in range(1,29):
    filename=filenames[i]
    if filename[-2:]!='py':
        os.renames(filename,filename+'.py')

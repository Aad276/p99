import os
import shutil
import time

path=input("Path to the location to remove old files")
days=input("Delete files before :")

timeC=(time.time())-1*86400

for filename in os.listdir(path):
    if os.path.getmtime(os.path.join(path,filename))<timeC:
        if os.path.isFile(os.path.join(path,filename)):
            print(filename)
            os.remove(os.path.join(path,filename))
        elif os.path.isdir(os.path.join(path,filename)):
            print (filename)
            shutil.rmtree(os.path.join(path,filename))



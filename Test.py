import time
import datetime
import os
from os import walk

start = datetime.datetime.now()
for (dirpath, dirnames, filenames) in walk("D:\\"):
    for dirname in (dirnames):
        try:
            atime = os.path.getatime(os.path.join(dirpath, dirname))
            if start- datetime.timedelta(days=1)< datetime.datetime.fromtimestamp(atime):
                print (os.path.join(dirpath, dirname)
                       + " changed " + time.ctime(os.path.getctime(os.path.join(dirpath, dirname)))
                       + " modified " + time.ctime(os.path.getmtime(os.path.join(dirpath, dirname)))
                       + " accessed " + time.ctime(os.path.getatime(os.path.join(dirpath, dirname))))
        except IOError:
            print ("something wrong with " + dirname)
print (start)
print (datetime.datetime.now())


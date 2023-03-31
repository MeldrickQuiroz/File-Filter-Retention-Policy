import os, fnmatch, shutil, datetime, time, sys
from datetime import date

#This is the directories that you will want to move the files from and to
src_path = input ("Enter source directory: ")
dst_path = input ("Enter destination directory: ")

#How old do you want these file to be
retentionPolicy = input ("Enter retention policy: ")

#the type of file you want to retrieve
pattern = "*.mov*"

todayDate = date.today()
deltaDate = datetime.timedelta(int(retentionPolicy))
pastRetention = todayDate - deltaDate

#For loop goes through every file and directories from the source directory
for dirPath, dirNames, fileNames in os.walk(src_path):
        for filename in fileNames:
            fullPaths = os.path.join(dirPath, filename)
            fileInfo = os.stat(fullPaths)
            fileTime = fileInfo.st_birthtime
            creation = time.strftime('%m %d %Y', time.gmtime(fileTime))
            created_date = datetime.datetime.strptime(creation, '%m %d %Y').date()
            
            #this IF statement is checking to see if it meets the criteria of the type of file and the date the file was created
            if fnmatch.fnmatch(filename, pattern) and created_date < pastRetention:
                shutil.move(fullPaths, dst_path)
            else:
                continue


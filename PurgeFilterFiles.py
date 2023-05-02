import os
import fnmatch
import shutil
import datetime
import time
import sys

#This is the directories that you will want to move the files from and to
src_path = input("Enter source directory: ")
dst_path = input("Enter destination directory: ")

#How old do you want these file to be
retentionPolicy = input("Enter retention policy: ")

#the type of file you want to retrieve
pattern = "*.mov*"

todayDate = datetime.date.today()
deltaDate = datetime.timedelta(int(retentionPolicy))
pastRetention = todayDate - deltaDate
MOVfilesize = 25

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
            filesize = os.path.getsize(fullPaths)
            sizeGB = filesize / (1024*1024*1024)
            if sizeGB >= MOVfilesize:
                dest_file_path = os.path.join(dst_path, filename)
                if os.path.exists(dest_file_path):
                    # if a file with the same name already exists in the destination directory, rename the file being moved
                    file_name, file_extension = os.path.splitext(filename)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    new_filename = file_name + '_' + timestamp + file_extension
                    dest_file_path = os.path.join(dst_path, new_filename)
                shutil.move(fullPaths, dest_file_path)
            else:
                continue
        else:
            continue

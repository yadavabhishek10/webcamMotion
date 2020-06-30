# To browse all the captured images and videos in the folder
import os

list_of_files = []
for i in os.scandir("D:\DataScience\cv_project\Captured"):
    if i.is_file():
        list_of_files.append(os.path.basename(i))
        # print('File: ' + os.path.basename(i))

print("Files: {0}".format(list_of_files))

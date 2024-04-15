#This is for testing purpose for listing of all files on desktop.

import os

drive_path = '/home/nag2mani/sitare/sem4/seir/SearchEngines_and_InformationRetrieval'
for root, dirs, files in os.walk(drive_path):
    # for file in files:
        # file_list.append(os.path.join(root, file))
        # print(file)
    # print(type(i))
    print(root)
    print(dirs)
    print(files)
    print("--------------------------------------------------------")



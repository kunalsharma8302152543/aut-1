import os
import shutil

from_dir="Downloads"
to_dir="Documents"

list_of_files= os.listdir(from_dir)
#print(list_of_files)


for i in list_of_files:
    os.path.splitext()
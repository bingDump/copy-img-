import shutil
import glob
import pandas as pd

path_base = glob.glob('foldername/*')
path_to = 'folder_name/'

data = pd.read_excel('file_excel_name.xlsx', sheet_name=0)
images_name = data['header_name'].tolist()

print(f"{len(path_base)}\timages in folder base")
print(f"{len(images_name)}\timages list to copy")

count = 0
for image_name in images_name:
    for file in path_base:
        if image_name in file:
            shutil.copy(file, path_to)
            count += 1
        else:
            continue

print(f"{count} files copied to {path_to}")
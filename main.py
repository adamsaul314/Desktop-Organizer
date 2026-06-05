import os
import shutil

documentPath = "./Documents"
imagePath = "./Images"

os.chdir("C:\\Users\\adams\\Desktop\\Desktop-Organizer\\Test_Desktop")

current_directory = os.getcwd()

dir_list = os.listdir(current_directory)

print(dir_list)

fileToFolder = {
    "pdf": "Documents",
    "txt": "Documents",
    "pdf": "Documents",
    "webp": "Images",
    "jpg": "Images"
}

os.makedirs(documentPath, exist_ok=True)
os.makedirs(imagePath, exist_ok=True)

for filename in dir_list:
    if filename.endswith(".pdf") or filename.endswith(".txt"):
        try:
                shutil.move(current_directory, documentPath)
                print("Files sorted into Documents directory!")
        except FileExistsError:
                print("Duplicate Files Present")
        break





for filename in dir_list:
    if filename.endswith(".webp") or filename.endswith(".jpg"):
        try:
                shutil.move(current_directory, imagePath)
                print("Files sorted into Images directory!")
        except FileExistsError:
                print("Duplicate Files Present")
        break
            
        
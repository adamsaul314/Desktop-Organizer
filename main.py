import os

os.chdir("C:\\Users\\adams\\Desktop\\Desktop-Organizer\\Test_Desktop")

current_directory = os.getcwd()

dir_list = os.listdir(current_directory)

print(dir_list)


#move PDFs out of Pictures and into a PDF folder in the Documents directory
import os
import shutil

#Get current directory
cur_dir = os.getcwd()
print(f"Current directory: {cur_dir}")

print("Do you want to change directories? Y/N")
response = input()
if response == "Y":
    print("Enter the new directory path")
    new_dir = input().replace("\\", "/")
    os.chdir(new_dir)
    print(f"Updated directory: {os.getcwd()}")

if response == "N":
    new_dir = cur_dir
    print(f"Continuing with current directory: {new_dir}")

else:
    print("Invalid input, Closing script...")
    exit()

# #set new directory and destination directory for file transfer
# dest_dir = "C:/Users/Anthem/Documents/pdffile"

# #go through each pic in Pictures and if it ends with .pdf move to new folder
# for pic in os.listdir():
#     source_path = os.path.join(new_dir, pic)
#     dest_path = os.path.join(dest_dir, pic)

#     if pic.endswith (".pdf"):
#         shutil.move(source_path, dest_path)
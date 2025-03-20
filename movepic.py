#move PDFs out of Pictures and into a PDF folder in the Documents directory
import sys
import os
import shutil

def moveFiles(src_dir):
    #set new directory and destination directory for file transfer
    print("Where would you like to move the files? Enter destination path: ")
    dest_dir = input().replace("\\", "/").strip('"').strip("'")

    #go through each pic in Pictures and if it ends with .pdf move to new folder
    for file in os.listdir():
        src_path = os.path.join(src_dir, file)
        dest_path = os.path.join(dest_dir, file)

        if file.endswith (".pdf"):
            shutil.move(src_path, dest_path)
    return dest_dir

def main():
    #Get current directory
    cur_dir = os.getcwd()
    print(f"Current directory: {cur_dir}")

    print("Do you want to change directories? Y/N")
    response = input()
    if response == "Y":
        print("Enter the new directory path: ")
        new_dir = input().replace("\\", "/").strip('"').strip("'")
        os.chdir(new_dir)
        print(f"Updated directory: {os.getcwd()}")
        dest_dir = moveFiles(new_dir)
        print(f"Files Successfully moved to {dest_dir}")
        sys.exit()

    if response == "N":
        print(f"Continuing with current directory: {cur_dir}")
        dest_dir = moveFiles(cur_dir)
        print(f"Files Successfully moved to {dest_dir}")
        sys.exit()

    else:
        print("Invalid input, Closing script...")
        sys.exit()

if __name__ == "__main__":
    main()
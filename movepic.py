#move files out of one directory and into a folder specified by the user. The user can change the filetype in the moveFiles function.
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

        #Here the user can change the file extension for the filetype they are trtying to move
        if file.endswith (".pdf"):
            shutil.move(src_path, dest_path)
    return dest_dir

def main():
    #Get current directory
    cur_dir = os.getcwd()
    print(f"Current directory: {cur_dir}")

    print("Do you want to change directories? Y/N")
    response = input()
    
    #'Y' if the user wants to change the current directory they are in. Copy and paste the path and it will be formatted correctly.
    if response == "Y":
        print("Enter the new directory path: ")
        new_dir = input().replace("\\", "/").strip('"').strip("'")
        os.chdir(new_dir)
        print(f"Updated directory: {os.getcwd()}")
        dest_dir = moveFiles(new_dir)
        print(f"Files Successfully moved to {dest_dir}")
        sys.exit()

    #Keep same directory
    if response == "N":
        print(f"Continuing with current directory: {cur_dir}")
        dest_dir = moveFiles(cur_dir)
        print(f"Files Successfully moved to {dest_dir}")
        sys.exit()

    #if response is not 'Y' or 'N' the script will close
    else:
        print("Invalid input, Closing script...")
        sys.exit()

if __name__ == "__main__":
    main()

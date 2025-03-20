# Repository for Python Automation
Welcome to my Python Automation scripts for Windows! Here I will be uploading scripts that automate task for your Windows machine. I will use the README.md to go into detail about each script.

## movepic.py
This script assist the user in moving multiple filetypes from one directory to another. The script will display your current directory (where the script resides on your PC) and ask if you would like to keep it the same or change it. 
    
    cur_dir = os.getcwd()
    print(f"Current directory: {cur_dir}")

    print("Do you want to change directories? Y/N")
    response = input()

### Source directory
If the response in 'Y' you can input the path either by typing it out or 'Copy as path' from the directory you would like to start in, movepic.py will format the input to a valid path structure. It will also update to the new directory.

    if response == "Y":
        print("Enter the new directory path: ")
        new_dir = input().replace("\\", "/").strip('"').strip("'")
        os.chdir(new_dir)

'N' response will stay in the current directory and a response that is not 'Y' or 'N' will close the script.

    if response == "N":
        print(f"Continuing with current directory: {cur_dir}")

    else:
        print("Invalid input, Closing script...")
        sys.exit()

### Destination directory
The `moveFiles` function calls for the destination directory and similar to change directory response you can type of 'Copy as Path'.

    print("Where would you like to move the files? Enter destination path: ")
    dest_dir = input().replace("\\", "/").strip('"').strip("'")

### Moving the files
The script will go through every file in your source directory and if the filetype matches the extension in the if-statement it will be moved to the destination directory.

    for file in os.listdir():
        src_path = os.path.join(src_dir, file)
        dest_path = os.path.join(dest_dir, file)

Here you can change the filetype, the default is PDF

    if file.endswith (".pdf"):
        shutil.move(src_path, dest_path)
    return dest_dir

### Successful file transfer
When all files are read and/or moved the script will reply with a success message and the destination directory. The script will then exit.

    print(f"Files Successfully moved to {dest_dir}")
    sys.exit()

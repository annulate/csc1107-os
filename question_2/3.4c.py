# Task 3.4c: Count and compress .txt files into mytxt.zip (Self-developed Python Code)

import os
import zipfile

# Simulate the creation of .txt files with contents
def create_txt_files():
    
    # Create a dictionary to link 5 different .txt file names and add values inside them
    files = {
        "file1.txt": "test1",
        "file2.txt": "test2",
        "file3.txt": "test3",
        "notes1.txt": "notes1",
        "notes2.txt": "notes2"
    }

    # Use a loop to create the 5 .txt files and add their values inside
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content + "\n")


def cwd():
    cwd = os.getcwd()

    return cwd

def txt_files(cwd):
    txt_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]

    return txt_files

def txt_files_counter(txt_files):
    num_txt_files = len(txt_files)
    
    if num_txt_files == 0:
        print("No files ending with the extension '.txt' found in the directory")
    
    else:
        print(f"Total number of '.txt' files in the zip: {num_txt_files}")
        print(f"Printing list of .txt files")
        for i in range(0, num_txt_files, 1):
            print(f"{txt_files[i]}")
        print(f"There are number of {num_txt_files} .txt files and compressed into a .zip file.")

def zip_files(txt_files, cwd):

    if len(txt_files) == 0:
        print("No '.txt' files to compress")
        return
    zip_filename = input("Enter your zip file name without extension: ") + '.zip'

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for txt_file in txt_files:
            file_path = os.path.join(cwd, txt_file)
            zipf.write(file_path, arcname=txt_file)


create_txt_files()
cwd = cwd()
txt_files = txt_files(cwd)
zip_files(txt_files,cwd)
txt_files_counter(txt_files)

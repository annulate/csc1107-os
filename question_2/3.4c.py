# Task 3.4c: Count and compress .txt files into mytxt.zip (Self-developed Python Code)

import os
import zipfile

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

def zip_files(txt_files, cwd):

    if len(txt_files) == 0:
        print("No '.txt' files to compress")
        return
    zip_filename = input("Enter your zip file name without extension: ") + '.zip'

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for txt_file in txt_files:
            file_path = os.path.join(cwd, txt_file)
            zipf.write(file_path, arcname=txt_file)


cwd = cwd()
txt_files = txt_files(cwd)
txt_files_counter(txt_files)
zip_files(txt_files,cwd)
# Task 3.4d: Count and compress .txt files into mytxt.zip (GenAI-generated Python Code)

import os
import zipfile

def compress_txt_files():
    # Ask the user for the desired zip file name (without extension)
    zip_name = input("Enter the name for the zip file (without the .zip extension): ")

    # Add the .zip extension to the user input
    zip_name = f"{zip_name}.zip"

    # List all .txt files in the current directory
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]

    # Count the number of .txt files
    txt_count = len(txt_files)

    # Check if there are any .txt files
    if txt_count > 0:
        # Create a zip file with the user-provided name and add all .txt files
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for txt_file in txt_files:
                zipf.write(txt_file, os.path.basename(txt_file))
        
        # Print the result
        print(f"There are {txt_count} .txt files and compressed into {zip_name}.")
    else:
        # If no .txt files are found, print a message
        print("No .txt files found in the current directory.")

# Call the function
compress_txt_files()

#!/bin/bash

# Ask the user for the desired zip file name
read -p "Enter the name for the zip file (without the .zip extension): " zip_name

# Add the .zip extension to the user input
zip_name="$zip_name.zip"

# List all .txt files in the current directory
txt_files=(*.txt)

# Count the number of .txt files
txt_count=${#txt_files[@]}

# Check if there are any .txt files
if [ $txt_count -gt 0 ]; then
    # Compress all .txt files into the user-provided zip file name
    zip "$zip_name" "${txt_files[@]}"

    # Print the result
    echo "There are $txt_count .txt files and compressed into $zip_name."
else
    # If no .txt files are found, print a message
    echo "No .txt files found in the current directory."
fi

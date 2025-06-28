#!/bin/bash

# List all .txt files in the current directory
txt_files=(*.txt)

# Count the number of .txt files
txt_count=${#txt_files[@]}

# Check if there are any .txt files
if [ $txt_count -gt 0 ]; then
    # Compress all .txt files into mytxt.zip
    zip mytxt.zip "${txt_files[@]}"

    # Print the result
    echo "There are $txt_count .txt files and compressed into a .zip file."
else
    # If no .txt files are found, print a message
    echo "No .txt files found in the current directory."
fi

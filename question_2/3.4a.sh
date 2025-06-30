#!/bin/bash
# Task 3.4a: Count and compress .txt files

# Make some sample test files
echo "test1" > file1.txt
echo "test2" > file2.txt  
echo "test3" > file3.txt
echo "notes" > notes.txt

# Get zip name from user
read -p "Enter the name for the zip file (without the .zip extension): " name
name="$name.zip"

# Find .txt files
txt_files=(*.txt)
txt_count=${#txt_files[@]}

# List them
echo "Found .txt files:"
for file in "${txt_files[@]}"; do
    echo "$file"
done

# Zip them up
powershell.exe -Command "Compress-Archive -Path '*.txt' -DestinationPath '$name' -Force"

# Remove the .txt files after zipping
rm *.txt

# Show result
echo "There are $txt_count .txt files and compressed into $name file."
echo "Original .txt files have been removed."
#!/bin/bash
# Task 3.4b: Count and compress .txt files into mytxt.zip (GenAI-generated Bash Shell Script)

# Create sample files with various extensions
echo "Creating sample files with various extensions..."
echo "This is document 1 content" > document1.txt
echo "This is document 2 content" > document2.txt
echo "Meeting notes from today" > meeting_notes.txt
echo "Project readme information" > readme.txt
echo "Important todos and tasks" > todo.txt
echo "Sample files created successfully."
echo ""

# Ask the user for the desired zip file name
read -p "Enter the name for the zip file (without the .zip extension): " zip_name

# Add the .zip extension to the user input
zip_name="$zip_name.zip"

# List all .txt files in the current directory
txt_files=(*.txt)

# Count the number of .txt files
txt_count=${#txt_files[@]}

# Check if there are any .txt files and if they actually exist
if [ $txt_count -gt 0 ] && [ -f "${txt_files[0]}" ]; then
    # Display the found .txt files
    echo "Found .txt files:"
    for file in "${txt_files[@]}"; do
        echo "  - $file"
    done
    echo ""
    
    # Use PowerShell to compress all .txt files (works in Git Bash on Windows)
    powershell.exe -Command "Compress-Archive -Path '*.txt' -DestinationPath '$zip_name' -Force"

    # Print the result
    echo "There are $txt_count .txt files and compressed into $zip_name."
else
    # If no .txt files are found, print a message
    echo "No .txt files found in the current directory."
fi
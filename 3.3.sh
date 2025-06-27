#!/bin/bash

# Indexed array to store numbers
list=()

# Collect numbers from input
read -p "Enter numbers separated by spaces: " numbers

# Convert and split the input into the array and add to list
for value in $numbers; do
    # Check if value is a valid number
    if [[ ! "$value" =~ ^[0-9]+$ ]]; then
        echo "There are invalid numbers in your input, please enter valid numbers."
        echo "Terminating script."
        exit 1 
    fi
    list+=("$value")  # Append the valid number to the list
done

# Print the list with commas and square brackets
echo "Your list is: [$(printf "%s, " "${list[@]}" | sed 's/, $//')]"

# Ask the user to input a target value and store as input called target
read -p "Enter value to check: " target

# Initialize an associative array (hash map)
declare -A check_map

# Find the complement
for num in "${list[@]}"; do
    complement=$(( target - num ))

    # Check if the complement is already stored in the hash map, if found, echo
    if [[ -v check_map["$complement"] ]]; then
        echo "There are two numbers in the list summing to the keyed-in number $target"
        exit 0  # Terminate the script once the answer is found
    fi

    # If the number is not found yet, store it in the map
    check_map["$num"]=1
done

# If no two values sum to the target
echo "There are no two numbers in the list summing to the keyed-in number $target"

exit 0
#!/bin/bash

# Ask the user to input a list of numbers separated by spaces
echo "Enter a list of numbers separated by spaces:"
read -a numbers

# Ask the user to input the target sum
echo "Enter a number to check if any two numbers in the list sum to it:"
read target_sum

# Initialize a flag to track if a pair is found
found_pair=false

# Loop through the list and check for pairs
for ((i = 0; i < ${#numbers[@]}; i++)); do
    for ((j = i + 1; j < ${#numbers[@]}; j++)); do
        # Check if the sum of numbers[i] and numbers[j] equals the target_sum
        if (( ${numbers[i]} + ${numbers[j]} == target_sum )); then
            found_pair=true
            break 2
        fi
    done
done

# Output the result
if [ "$found_pair" = true ]; then
    echo "There are two numbers in the list summing to the keyed-in number $target_sum."
else
    echo "There are no two numbers in the list summing to the keyed-in number $target_sum."
fi

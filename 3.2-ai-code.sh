#!/bin/bash

# Prompt the user to enter a list of numbers
echo "Enter a list of numbers separated by spaces:"
read -a numbers

# Initialize largest number as the first element
largest_number=${numbers[0]}

# Loop through the list to find the largest number
for num in "${numbers[@]}"
do
  if (( num > largest_number )); then
    largest_number=$num
  fi
done

# Print the largest number
echo "$largest_number is the largest number"

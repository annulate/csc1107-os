#!/bin/bash

#Prompt to enter integers separated by spaces
read -p "Enter numbers of the list separated by spaces:" -a num_list

#Check if entered is an integer
for num in "${num_list[@]}"; do
    if ! [["$num" =~ ^-?[0-9]+$]]; then
        echo "Error: '$num' is not a valid integer"
        exit 1
    fi
#Print the list
echo "You entered: ${num_list[@]}"

#Initialise largest number as first number in the list
largest =${num_list[0]}

for num in "${numlist[@]}"; do
    if [ "$num" -gt "$largest"]; then
        largest=$num
    fi
done

echo "$largest is the largest number"

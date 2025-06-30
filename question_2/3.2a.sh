#!/bin/bash
# Task 3.2a: Find largest number (Self-developed Bash Shell Script)

read -p "Enter numbers of the list separated by spaces: " -a num_list
echo "You entered: ${num_list[@]}"

# Add this after reading input
for num in "${num_list[@]}"; do
    if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
        echo "Error: '$num' is not a valid integer. Please enter integers only."
        exit 1
    fi
done

largest=${num_list[0]}

for num in "${num_list[@]}"; do
    if [ "$num" -gt "$largest" ]; then
        largest=$num
    fi
done

echo "$largest is the largest number"
#!/bin/bash
#Task 3.1b: Check user input for prime number (GenAI-generated Bash Shell Script)

# Function to check if a number is prime
is_prime() {
    local n=$1
    if ((n <= 1)); then
        return 1
    fi
    if ((n == 2)); then
        return 0
    fi
    if ((n % 2 == 0)); then
        return 1
    fi
    for ((i = 3; i * i <= n; i += 2)); do
        if ((n % i == 0)); then
            return 1
        fi
    done
    return 0
}

# Prompt user for input
read -p "Enter a number: " num

# Call function and check if prime
if is_prime $num; then
    echo "The keyed-in number $num is a prime number."
else
    echo "The keyed-in number $num is not a prime number."
fi

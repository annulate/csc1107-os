#!/bin/bash

# 3.1b-ai-code.sh
# Function to check if a number is prime (ai-generated)

is_prime() {
    local num=$1
    if ((num <= 1)); then
        echo "$num is not prime"
        return
    fi
    for ((i = 2; i * i <= num; i++)); do
        if ((num % i == 0)); then
            echo "$num is not prime"
            return
        fi
    done
    echo "$num is prime"
}

# Read input from user
read -p "Enter a number: " number

# Check if the number is prime
is_prime $number

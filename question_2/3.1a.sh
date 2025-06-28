#!/bin/bash
#Task 3.1a: Check user input for prime number (Self-generated Bash Shell Script)

# Function for check if a input is prime or not
checking_for_prime() {
    local usernum=$1

    if ((usernum == 0)) || ((usernum == 1)); then
        echo "The keyed in number $usernum is NOT a prime number."
    else
        for ((x = 2; x < usernum; x++)); do
            if ((usernum % x == 0)); then
                echo "The keyed in number $usernum is NOT a prime number."
                return
            fi
        done
        echo "The keyed in number $usernum is a prime number."
    fi
}

#Takes in user input
read -p "Enter a number: " usernum

if [[ $usernum =~ ^-?[0-9]+$ ]]; then
    checking_for_prime $usernum
#to catch invalid input
else
    echo "Please enter an integer!"
fi

#!/bin/bash

# 3.1a-selfdev-code.sh
# Function to check if a number is prime (self-developed)

checking_for_prime(){
    usernum=$1
    if [ $usernum -le 1 ]; then
        echo "The keyed in number $usernum is NOT a prime number."
    else
        for (( x=2; x<usernum; x++ )); do
            if [ $(( usernum % x )) -eq 0 ]; then
                echo "The keyed in number $usernum is NOT a prime number."
                return
            fi
        done
        echo "The keyed in number $usernum is a prime number."
    fi
}

#read input and check if it is prime
read -p "Enter a number: " usernum
checking_for_prime $usernum
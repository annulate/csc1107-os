<<<<<<<< Updated upstream:question_2/3.1d-ai-code.py
# 3.1d ai-code.py
# Function to check if a number is prime (ai-generated)
========
# Task 3.1d: Check user input for prime number (AI-generated Python code)
>>>>>>>> Stashed changes:question_2/3.1d.py

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Main program
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"The keyed-in number {num} is a prime number.")
    else:
        print(f"The keyed-in number {num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")

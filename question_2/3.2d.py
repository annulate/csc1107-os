# Task 3.2d: Find largest number (GenAI-generated Python code)


def find_largest_number():
    # Get user input
    numbers_input = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    numbers = list(map(int, numbers_input.split()))
    
    # Find the largest number
    largest_number = max(numbers)
    
    # Print the message
    print(f"{largest_number} is the largest number")

# Call the function
find_largest_number()

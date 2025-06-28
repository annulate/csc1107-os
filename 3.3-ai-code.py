def check_sum_to_key():
    # Get the list of numbers from the user
    numbers_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers_input.split()))  # Convert the input string to a list of integers

    # Get the target sum from the user
    target_sum = int(input("Enter the target sum: "))
    
    # Create a set to store numbers we've already seen
    seen_numbers = set()

    # Flag to track if we found a pair
    found_pair = False

    # Iterate through the list to find two numbers that sum to target_sum
    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            found_pair = True
            break
        seen_numbers.add(num)

    # Print the result
    if found_pair:
        print(f"There are two numbers in the list summing to the keyed-in number {target_sum}")
    else:
        print(f"There are no two numbers in the list summing to the keyed-in number {target_sum}")

# Example usage
check_sum_to_key()

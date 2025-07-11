# Function to add numbers into a list separated by spacebar
def add_to_list():
    while True:
        try:
            input_num_str = input("Enter numbers separated by spaces: ")
            # Split the input string into a list of number strings
            num_str = input_num_str.split()
            
            # Convert each string into an integer and add to the list
            numlist = []
            for s in num_str:
                numlist.append(int(s))
                
            print("Your list is: ", numlist)
            return numlist
        except ValueError:
            print("Error: Please enter only valid integers separated by spaces.")
            
# Function to check 2 numbers
def num_checker(numlist):
    while True:
        try:
            target = int(input("Enter value to check: "))  # Validate target as an integer
            if len(numlist) < 2:  # Handle the case where there are fewer than 2 numbers in the list
                print("Error: The list needs to have at least 2 numbers to check the sum.")
                return
            
            seen = set()
            for num in numlist:
                complement = target - num
                if complement in seen:
                    # If a pair is found, print a success message
                    print("There are two numbers in the list summing to the keyed-in number %d" % target)
                    return
                seen.add(num)
                
            # If no pair is found, print a message saying so
            print("There are no two numbers in the list summing to the keyed-in number %d" % target)
            return
        
        except ValueError:
            print("Error: Please enter a valid integer for the target value.")

# Main program to get the list and check for the target sum
numlist = add_to_list()
num_checker(numlist)

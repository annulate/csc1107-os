# Task 3.2c: Find largest number (Self-developed Python Code)

#Function to add numbers into a list separated by spacebar
def add_to_list():
    while True:
        try:
            input_num_str = input("Enter numbers separated by spaces: ")
            # Split the input string by spaces
            num_str = input_num_str.split()
            
            # Convert each item to an integer, and handle errors
            numlist = []
            for s in num_str:
                numlist.append(int(s))  # Convert to integer
            print("Your list is: ", numlist)
            return numlist
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

#Function to find largest number
def largest(numlist):
    
    #If list empty
    if len(numlist) == 0:
        return None
    #If list not empty
    largest = numlist[0] #Assume largest number is first number
    for num in numlist[1:]:
        if num > largest:
            largest = num
    print("%d is the largest number" %largest)

numlist = add_to_list()
largest(numlist)
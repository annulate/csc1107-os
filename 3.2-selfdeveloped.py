#Function to add numbers into a list separated by spacebar
def add_to_list():
    input_num_str = input("Enter numbers separated by spaces: ")
    num_str = input_num_str.split()
    numlist = []
    for s in num_str:
        numlist.append(int(s))
    print("Your list is: ", numlist)
    return numlist

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
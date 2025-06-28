#Function to add numbers into a list separated by spacebar
def add_to_list():
    input_num_str = input("Enter numbers separated by spaces: ")
    num_str = input_num_str.split()
    numlist = []
    for s in num_str:
        numlist.append(int(s))
    print("Your list is: ", numlist)
    return numlist

#Function to check 2 numbers
def num_checker(numlist):
    target = int(input("Enter value to check: "))
    seen = set()

    for num in numlist:
        complement = target - num
        if complement in seen:
            print("There are two numbers in the list summing to the keyed-in number %d" %target)
            return
        seen.add(num)
    print("There are no two numbers in the list summing to the keyed-in number %d" %target)

numlist = add_to_list()
num_checker(numlist)
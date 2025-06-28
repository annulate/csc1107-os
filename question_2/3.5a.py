#Task 3.5a: FIFO Page Replacement Algorithm (Self-generated Python code)

#Function to set page frame capacity
def page_frame_capacity():
    while True:
        try:
            capacity = int(input("Enter the number of available frames in memory at a time (range in 3 - 6 page frames): "))
            if capacity <3 or capacity > 6:
                print("Enter a number between 3 - 6")
                continue
            else:
                break
        except ValueError:
            print("Invalid input, please only input integer.")
    return capacity

#Function to convert reference string into list
def reference_string_converter():
    while True: 
        try:
            reference_string = list(map(int, input("Enter reference string of referenced page numbers separated by commas, \",\" (range in 15 - 25 reference string): ").split(',')))
            if len(reference_string) < 15 or len(reference_string) > 25:
                print("Enter a string that has a range in 15 - 25 reference string")
                continue
            else:
                break
        except ValueError:
            print("Invalid input, only input a string of integers separated by commas \",\" ")
    return reference_string

#Print inputs
def printed_items(page_frame, reference_string):
    print(f"Page frame capacity is: {page_frame}")
    print(f"Reference string is: {reference_string}")
    print("Initial memory state: []")

#Used for counting of page faults
def counter(reference_string, page_frame_max):
    page_fault = 0 #Initialise page fault variable
    for page in reference_string:
        print(f"Referencing page: {page}")

        #Check through the memory set to see if page is in the frame
        if page not in memory:
            if len(storage) < page_frame_max:
                storage.append(page)
                memory.add(page)
            else:
                oldest = storage.popleft()
                memory.remove(oldest)
                storage.append(page)
                memory.add(page)
            page_fault += 1
        print(f"Page fault value: {page_fault}")





#Import doubled ended queue() function for use
from collections import deque
#Initialise for use
storage = deque() #Used to store n page frames
memory = set() #Used for lookup of storage 
page_frame_max = page_frame_capacity()
reference_string = reference_string_converter()
printed_items(page_frame_max, reference_string)
counter(reference_string, page_frame_max)


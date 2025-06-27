#Task 3.1c: Check user input for prime number (Self-developed Python Code)


def checking_for_prime(usernum):
    if usernum <= 1:
        print("The keyed in number", usernum ,"is NOT a prime number.")
    else:
        for x in range (2, usernum):
            if usernum % x == 0:
                print("The keyed in number", usernum ,"is NOT a prime number.")
                return
        else:
            print("The keyed in number", usernum ,"is a prime number.")
            
try:
    usernum = int(input("Enter a number: "))
    checking_for_prime(usernum)
except ValueError:
    print("Please enter an integer!")
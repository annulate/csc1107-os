#Question 2a: Check user input for prime number (Self-developed)

def checking_for_prime(usernum):
    if usernum <= 1:
        print(f"The keyed in number {usernum} is NOT a prime number.")
    else:
        for x in range (2, usernum):
            if usernum % x == 0:
                print(f"The keyed in number {usernum} is NOT a prime number.")
                return
        else:
            print(f"Yes, the keyed in number {usernum} is a prime number.")

    usernum = int(input("Enter a number: "))
    checking_for_prime(usernum)
except ValueError:
    print("Invalid input, please enter an integer!")

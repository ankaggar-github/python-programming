import sys
def collatz(number):
    if number % 2 == 0: # checking if number is even
        print(number // 2)
        return number // 2
    else: # checking if number is odd
        print(3 * number + 1)
        return 3 * number + 1
    
print("Please type a number:")
try:
    number = int(input())
    while True:
        if number != 1:
            number = collatz(number)
        else:
            print("We are on 1")
            sys.exit()
except ValueError:
    print("Error! Expecting only integer")

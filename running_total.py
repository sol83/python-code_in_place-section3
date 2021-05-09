"""
Running Total

Write a program that asks a user to continuously enter numbers and print out the running total, 
the sum of all the numbers so far. 
Once you get the program working, see if you can modify it so that the program stops when the user enters a 0.

Enter a value: 7
Running total is 7

Enter a value: 3
Running total is 10

Enter a value: 5
Running total is 15

Enter a value: 12
Running total is 27

Enter a value: 0
"""

def main():
    total = 0

    while True:
        value = int(input("Enter a value: "))

        if value == 0:
            # end the loop if the user types 0
            break

        # otherwise, calculate the new running total
        total += value
        print("Running total is " + str(total))
        print()

if __name__ == '__main__':
    main()
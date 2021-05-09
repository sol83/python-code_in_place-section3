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

Extension

If you solve this problem quickly, 
think about how you might extend the program to also keep track of the minimum and maximum numbers entered so far as well. 
A sample run of this extended program might look like this:


Enter a value: 42
Running total is 42
Maximum so far is 42
Minimum so far is 42

Enter a value: 3
Running total is 45
Maximum so far is 42
Minimum so far is 3

Enter a value: -6
Running total is 39
Maximum so far is 42
Minimum so far is -6

Enter a value: 0
"""

SENTINEL = 0

def main():
    value = int(input("Enter a value: "))
    total = value
    max_num = value
    min_num = value
    while value != SENTINEL:
        print("Running total is " + str(total))
        if value > max_num:
            max_num = value
        if value < min_num:
            min_num = value
        print("Maximum so far is", max_num)
        print("Minimum so far is", min_num)    
        print("")
        value = int(input("Enter a value: "))
        total += value
        
if __name__ == '__main__':
    main()
"""
FizzBuzz

In the game Fizz Buzz, players take turns counting up from one.
If a player’s turn lands on a number that’s divisible by 3,
they should say fizz instead of the number, and if it lands on a number that’s divisible by 5,
they should say buzz instead of the number. If the number is both a multiple of 3 and of 5,
they should say fizzbuzz instead of the number.

It is an interesting problem in control flow and parameter usage.
Write a program asks the user for an integer.
The program should count up until and including n,
fizzing and buzzing the correct numbers along the way. Once it's done,
the program should print how many numbers were fizzed, buzzed, or fizzbuzzed along the way.

Here's a sample run of the program:

Number to count to: 17
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizzbuzz
16
17

Num fizzed: 4
Num buzzed: 2
Num fizzbuzzed: 1
"""

FIZZ_NUM = 3
BUZZ_NUM = 5

def main():
    num = int(input("Number to count to: "))
    num_fizzed = 0
    num_buzzed = 0
    num_fizzbuzzed = 0
    for i in range(1, num + 1):
        if i % FIZZ_NUM == 0 and i % BUZZ_NUM != 0 :
            print("Fizz")
            num_fizzed += 1
        elif i % BUZZ_NUM == 0 and i % FIZZ_NUM != 0:
            print("Buzz")
            num_buzzed += 1
        elif i % FIZZ_NUM == 0 and i % BUZZ_NUM == 0:
            print("Fizzbuzz")
            num_fizzbuzzed += 1
        else:
            print(i)

# Or the following way, where the condition checking for fizzbuzz needs to be first:

        # if i % FIZZ_NUM == 0 and i % BUZZ_NUM == 0:
        #     print("Fizzbuzz")
        # elif i % FIZZ_NUM == 0:
        #     print("Fizz")
        # elif i % BUZZ_NUM == 0:
        #     print("Buzz")
        # else:
        #     print(i)

    print("")
    print("Num fizzed: " + str(num_fizzed))
    print("Num buzzed: " + str(num_buzzed))
    print("Num fizzbuzzed: " + str(num_fizzbuzzed))

if __name__ == '__main__':
    main()
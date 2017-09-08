"""
Ask the user for their input for the variables start and end (both integers)

make a for loop to go through each number from start to end
if number is divisable by 3 then
    print fizz
else if number is divisable by 5 then
    print buzz
else if number is divisable by 3 and 5 then
    print fizzbuzz
otherwise you just
    print the number
"""
import sys
startInput = int(sys.argv[1])
endInput = int(sys.argv[2])


def fizzbuzz(start, end):
    for num in range(start, end+1):
        if(num % 3 == 0 and num % 5 == 0):
            print("fizzbuzz")
        elif(num % 3 == 0):
            print("fizz")
        elif(num % 5 == 0):
            print("buzz")
        else:
            print(num)


fizzbuzz(startInput, endInput)

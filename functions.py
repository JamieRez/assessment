#Functions
import sys
userInput = int(sys.argv[1])

def fibonacci_iterative(num):
    #New to python, so I don't know how to check if a variable was not given a value. I could do that in javascript though
    currentNum = 1
    prevNum = 0
    for number in range(0, num):
        sum = currentNum + prevNum
        print(sum)
        prevNum = currentNum
        currentNum = sum

fibonacci_iterative(userInput)

#Recursion
def factorial_recursive(num):
    product = num
    for number in range(num-1, 0, -1):
        product = product * number
    print(product)


factorial_recursive(5)

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


#Recursion:
#After 30 minutes I realized I was going about it wrongly, I'm not sure how to do it

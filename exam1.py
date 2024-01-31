#write a program to calculate factorial of each number of list (contain n values from user) using function name FACT() which read a number and return factorial of that number.factorial of each number must be printed seperated by space
def FACT():
    tupl = eval(input("Enter a list: "))
    lis = list(tupl)
    facto = 1
    for i in lis:
        for i in range(1, i+1):
            facto = facto * i
        print(facto, end=" ")
        facto = 1

FACT()
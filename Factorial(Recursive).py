number= int(input("Write a number:  "))
def factorial(no): #basically this is the function that is used to calculate the factorial for the variable number
    if no == 1 or no == 0: #checks if the number inputted is 0 or 1
        return 1
    else:
        return no * factorial(no - 1)
print(f"{number}! = {factorial(number)}")
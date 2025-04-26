number = int(input("Write a number: "))
answer = len(str(abs(number)))
#the string function converts the numbers into a string to be counted
#the absolute is to make the number absolute and ignore the - sign as a character since it's a string
#the length function counts the no. of elements in the string
print(f"The number of digits in {number} is {answer}")
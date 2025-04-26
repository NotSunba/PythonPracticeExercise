my_marks = input("Write your marks:")
number = [int(mark) for mark in my_marks.split()] #changes your input from string to integers
total = sum(number) #adds all the numbers in the list
print(f"The total of your marks is {total}")
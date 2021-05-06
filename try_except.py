
#try-except case

try:
    number = int(input("Please enter a number: "))
    print(number)
except ValueError:
    print("Please enter valid number!")


try:
    number = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid")
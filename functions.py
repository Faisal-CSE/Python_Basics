
def say_hi():
    name = "Faisal Porag"
    print("Hello "+name)

say_hi()

def print_age(age):
    print("Your age is "+age)

int_age = input('Please enter your age: ')
print_age(int_age)

#Return Statement from a function
def cube(num):
    return num * num * num

result = cube(4)
print(result)
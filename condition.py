num1 = 2
num2 = 13

if num1 > num2:
    print("num1 is grater than num2")
elif num2 > num1:
    print("num2 is grater than num1")
else:
    print("Do nothing")


name = "Faisal1"
text = "I love my country1. Bangli is my language"
if name == "Faisal":
    print("Right")
else:
    print("Wrong")


if "country" in text:
    print("Exist")
else:
    print("Not exist")

if text.find("Bangla") > 0:
    print("Bangla exist")
else:
    print("Bangla not exist")


is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and also tall")
elif is_male or is_tall:
    print("You are male but not tall")
else:
    print("Nothing")


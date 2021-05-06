#While loop

i = 1
while i <= 10:
    print(i)
    print("\n")
    i+=1
print("---------------------------------")

#For loop
for p in "Faisal Porag":
    print(p)
print("---------------------------------")

friends = ["Jamal", "Kamal", "Rahim", "Habu", "Mia"]

for friend in friends:
    print(friend)

print("---------------------------------")

for l in range(15):
    print(l)

print("---------------------------------")

for l in range(5, 10):
    print(l)

print("---------------------------------")
friends2 = ["Jamal", "Kamal", "Rahim", "Habu", "Mia"]

for index in range(len(friends2)):
    print(friends2[index])

print("---------------------------------")

for p in range(6):
    if p == 0:
        print("First Iterations")
    else:
        print("Not first iterations")

    if p == 4:
        print("Stop loop ....")
        break
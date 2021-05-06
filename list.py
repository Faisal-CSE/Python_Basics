#List
#List is mutable (means u can change value after assign)

lucky_numbers = [14, 25, 64, 84, 59, 97]
team_mates = ['Porag', 'Sumi', 'Sudipto', 'Zamal', 'Kamal', 'Kamal']

print(lucky_numbers)

print(lucky_numbers[3])

#data[1] = 100

print(lucky_numbers)

print(lucky_numbers[3:])

print(lucky_numbers[2: 6])

#add two list
team_mates.extend(lucky_numbers)
print(team_mates)

#add new last of the list index
team_mates.append('Raju')
print(team_mates)

#Insert new data in a specific position in a list
team_mates.insert(2, 'Takrim')
print(team_mates)

#remove user from list
team_mates.remove('Sudipto')
print(team_mates)

#same data count from list
print(team_mates.count("Kamal"))

#Sort list
lucky_numbers.sort()
print(lucky_numbers)

#Copy any list
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)



#remove all user from list
team_mates.clear()
print(team_mates)
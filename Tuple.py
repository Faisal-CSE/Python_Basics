#Tuple is same as list. But tuple is immutable.Means u can not change value after assign

coordinates = (4, 2)
coordinates2 = [(4, 2), (58, 21, 21), (45.54, 51, 65)]

print(coordinates)
print(coordinates[0])


print(coordinates2)
print(coordinates2[2])
print(coordinates2[2][1])




#Error occured
#coordinates[1] = 25 #'tuple' object does not support item assignment
#print(coordinates)
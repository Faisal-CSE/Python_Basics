#Reading From file

emp_list_file = open("emp_list.txt", "r") #r for read
print(emp_list_file.readable())
#print(emp_list_file.read())
print(emp_list_file.readline())
print(emp_list_file.readlines())
for e in emp_list_file.readlines():
    print(e)
emp_list_file.close()

#open("emp_list.txt", "w") #w for write

emp_list_file_append_new = open("emp_list.txt", "a") #a for append
emp_list_file_append_new.write("Raza")
emp_list_file_append_new.close()


#open("emp_list.txt", "r+") #r+ for read and write
#print("Hello Hello Again!")


a = 1
b = 2
c = a + b

d = "Hello Hello!"

#print(d)

num_list = [1,2,3,4]

#for num in num_list:
	#print(num)

#print(num_list[0])
#print(num_list[1])
#print(num_list[2])
#print(num_list[3])

name_list = ["John", "Mary", "Tom"]

#for name in name_list:
#	for num in num_list:
#		print(name + str(num))

another_list = []
for num in num_list:
	another_list.append((num + 3)*2)

#print(another_list)

another_list_2 = [(num + 3)*2 for num in num_list]

#print(another_list_2)

#for num in another_list:
	#if(num > 11):
		#print("Big Number: " + str(num))
	#elif (num < 9):
		print("Small Number: " + str(num))
#
#def my_function():
	#print("Hello World!")
	#print("hello hello world")
	#print("hello hello hello world")

#my_function()

def augmented_numbers(num1, num2):
	return(num1 + num2) ** 2

print(augmented_numbers(1,2))

DRY = "Don't Repeat Yourself"


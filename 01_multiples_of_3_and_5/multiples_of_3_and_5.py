#initial value for our iterative variable
i = 0

#Creating the empty list
list = []

#Main function to check first if divisible by 3, then 5, store those that are, and add 1 to the iterative variable
for i in range(0, 1000):
	if i % 3 == 0:
		list.append(i)
	elif i % 5 == 0:
		list.append(i)
	else:
		i += 1

#Sum contents of "list" and store in new variable "total"
total = sum(list)

print(total)
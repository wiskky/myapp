'''
#This programe check for the duplicate number in the list and print it out.
num = [20,30,20,40,30,50,70,90,50,100, 700]

new = []

for i in num:
	n = num.count(i)
	if n > 1:
		if new.count(i) == 0:
			new.append(i)

print(new)

'''



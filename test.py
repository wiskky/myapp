#This program printing the even number from 1 to 30

a_list = []

for number in range(1,40):
    if number % 2 == 0:
        a_list.append(number)

print(a_list)
print(a_list)
print(a_list)
print(a_list)

#The below sprogram is the same as the first one as the above.

b_list = [ number for number in range(1, 30) if number % 2 == 0 ]
print(b_list)

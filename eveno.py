a_list = []

for number in range(1,30):
    if number % 2 == 0:
        a_list.append(number)

print(a_list)


#This sprogram is the same as the first one.

b_list = [ number for number in range(1, 30) if number % 2 == 0 ]
print(b_list)

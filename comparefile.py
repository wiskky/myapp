import sys

#This program is comparing the size of the list and tuple
#to know the one that has less bytes.

my_list = [0, 1, 2, 3, 4, 5, "Joy", False]
my_tuple = (0, 1, 2, 3, 4, 5, "Joy", False)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

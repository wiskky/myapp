import timeit

#This program calculate the execution time of the two statement

print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))

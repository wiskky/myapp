'''
Given a year, return the century it is in. The first century spans from 
the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17
Input/Output

'''


#challenge 1 from codesignal
#To check for leaf year

from math import *

def century(year):
	if (year % 100 == 0):  
		return (int(year/100))
	else:
		return(ceil(year/100))
	


print(century(1905))

print(century(1700))

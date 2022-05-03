'''
def checkPalindron(str):
	my = str
	rev = str[::-1]

	if my == rev:
		return 'It is a Palindron'
	else:
		return 'Not a palindron'

p = checkPalindron('saas')
print(p)
'''

"""
nums = [1,2,3,4,5,6]
w =  [a * b for a, b in zip(nums, nums[1:])]
print (min(list(w)))

"""



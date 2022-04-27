def checkPalindron(str):
	my = str
	rev = str[::-1]

	if my == rev:
		return 'It is a Palindron'
	else:
		return 'Not a palindron'

p = checkPalindron('saas')
print(p)
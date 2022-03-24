#how to use eval function in python
#This is just a skeleton program
#while True:
#	print(eval(input("Enter Expression: ")))

	

import os

from virtualenv import cli_run
#print(dir(os))

# list files and directories in the working directory

current_dir =os.getcwd()
for entry in os.listdir(current_dir):
	print(entry)
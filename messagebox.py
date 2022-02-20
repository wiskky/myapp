#using tkinter for message display on the screen
From tkinter import messagebox

userinput=input("Please enter your quotation ") #user input in the program
myText = "I have a dream to achieve"
ourinput=myText + userinput
messagebox.showinfo("Welcome",ourinput)

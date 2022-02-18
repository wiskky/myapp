#using tkinter 
From tkinter import messagebox

userinput=input("Please enter your quotation ")
myText = "I have a dream to achieve"
ourinput=myText + userinput
messagebox.showinfo("Welcome",ourinput)

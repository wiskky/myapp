'''''
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

p=MyClass()         #to access the main class variable
p.function()        #to access thr print varible in the function session

'''

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        #desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return(f"{self.name} is a {self.color} {self.kind} worth {self.value}")
        #return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.color = "Red"
car1.name = "Toyata" 
car2.color = "Blue"
car2.name = "Honda"
car2.value = 200000
print(car1.description())
print(car2.description())


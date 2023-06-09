# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name        
#         self. age = age

#     def speak(self):
#         print("Bark")    

class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")  

    def speak(self):
        print ("I don't know what to say")       

class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")      

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Alex", 19)
p.show()
p.speak()
c = Cat ("Jill", 15, "Black")
c.show()
c.speak()
d = Dog("Bill", 25)
d.show()
d.speak()

# position(class), name, age, level, salary
# class
class Software_engeneer:
    # instance attributes
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writting code...")

    def code_in_language(self, language):
        print(f"{self.name} is writting code in {language}...") 

    #  dunder method
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.level} level, and makes {self.salary}."

    #print all function 
    def print_all_engeneers(engeneers):
        for engeneer in engeneers:
            print(engeneer)

# instance 
engeneers = [Software_engeneer("Wayne", 25, "Junior", 3000),
            Software_engeneer("John", 30, "Senior", 5000),
            Software_engeneer("Richard", 30, "Senior", 7000)]

Software_engeneer.print_all_engeneers(engeneers)
engeneers[0].code()
engeneers[0].code_in_language("Java")
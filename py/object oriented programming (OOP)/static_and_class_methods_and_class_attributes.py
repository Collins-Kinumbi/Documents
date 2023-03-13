class Person:
    number_of_people = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.number_of_people +=1

p1 = Person("Bruce")
print(Person.number_of_people)
p2 = Person("Wayne")
print(Person.number_of_people)
class Employee:
    # class variable number of employees
    num_of_emps = 0
    def __init__(self, first_name, last_name, pay) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name +"."+last_name+"@company.com"
        Employee.num_of_emps +=1 
    
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def income(self):
        return "{} earns {}".format(self.fullname(), self.pay )    
    
    def mail(self):
        return self.email
    


Employees = [
    Employee("Tim", "Drake", 10000),
    Employee("Jason", "Wayne", 120000),
    Employee("Bruce", "Tim", 100000)
]        

print(Employees[1].fullname())
print (Employees[1].income())
print (Employees[1].mail())
print (Employee.num_of_emps)
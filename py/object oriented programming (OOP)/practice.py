class User:
    def log(self):
        print(self)


class Customer(User):
    def __init__(self, name, membership_type) -> None:
        self.name = name
        self.membership_type = membership_type

    @property
    # getter
    def name(self):
        return self._name    

    @name.setter
    # setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        self.membership_type = new_membership  

    def __str__(self) -> str:
        return self.name +" "+self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    def __eq__(self, other) -> bool:
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        else:
            return False

customers = [Customer("Collins", "Silver"),
             Customer("Kevin", "Gold"),
             Customer("Bradley", "Platnum")]

Customer.print_all_customers(customers)

print(customers[0]==customers[1])

customers[0].log()
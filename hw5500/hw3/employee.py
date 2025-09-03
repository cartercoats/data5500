class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def give_raise(self,percent):
        return self.salary*percent

john = Employee("John",5000)

print(john.give_raise(1.1))
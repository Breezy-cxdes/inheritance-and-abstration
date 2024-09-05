class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("My name is", self.name)
        print("My ID number is", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post

    def display_employee(self):
        self.display()  # Display the person's details
        print("Salary is", self.salary)
        print("Post is", self.post)

# Create an employee object
obj = Employee("John", "2345", "500", "Intern")
obj.display_employee()

      


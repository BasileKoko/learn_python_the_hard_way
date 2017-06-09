class Employee:
    def __init__(self, firstname, surname,  age):
      self.firstname = firstname
      self.surname = surname
      self.age = age

    def fullname(self):
      return self.firstname + " " + self.surname

employee1 = Employee('Corey', 'Wayne', 20)
print employee1.fullname()
print employee1.age

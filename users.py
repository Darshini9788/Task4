# users.py
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)  # reuse parent constructor
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)  # reuse parent constructor
        self.salary = salary


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)  # reuse Faculty constructor
        self.duration = duration
        
        
        # task2
       
from abc import ABC, abstractmethod


# Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# child class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

  
    def get_details(self):
        return f"User: {self.name}, ID: {self.id}"


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

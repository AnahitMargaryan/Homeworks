
from abc import ABC, abstractmethod
class MathematicFunctions(ABC):

    @abstractmethod
    def sum_calculation(self):
        pass
    def average_calculation(self):
        pass

class Salary(MathematicFunctions):
    def __init__(self, salary1, salary2, salary3):
        self.salary1 = salary1
        self.salary2 = salary2
        self.salary3 = salary3

    def sum_calculation(self):
        return self.salary1 + self.salary2 + self.salary3
    def average_calculation(self):
        return (self.salary1 + self.salary2 + self.salary3) / 3
    
class Grade(MathematicFunctions):
    def __init__(self, grade1, grade2, grade3):
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def sum_calculation(self):
        return self.grade1 + self.grade2 + self.grade3
    def average_calculation(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3  # args, list
    
salary_object = Salary(1500,2650,3120)
print(salary_object.sum_calculation())
print(salary_object.average_calculation())

grade_object = Grade(7,8,9)
print(grade_object.sum_calculation())
print(grade_object.average_calculation())

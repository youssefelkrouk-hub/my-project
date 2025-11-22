class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"{self.name} est d'age de {self.age} ans "
    def __eq__(self,other):
        return (self.name==other.name and self.age==other.age) 

# Définition des exceptions
# class SalaryError(ValueError):
#     pass

# class BonusError(SalaryError):
#     pass

# # Classe Employee
# class Employee:
#     MIN_SALARY = 30000
#     MAX_BONUS = 5000

#     def __init__(self, name, salary):
#         if salary < Employee.MIN_SALARY:
#             raise SalaryError("Salary is too low!")
#         self.name = name
#         self.salary = salary

#     def give_bonus(self, amount):
#         if amount > Employee.MAX_BONUS:
#             raise BonusError("Bonus is too high!")
#         self.salary += amount
#         return self.salary


# # --- Cas 1 : Parent (SalaryError) avant l'enfant (BonusError)
# print("Cas 1 : Parent avant enfant")
# emp = Employee("Katze Rik", 50000)
# try:
#     emp.give_bonus(7000)   # Déclenche BonusError
# except SalaryError:
#     print("SalaryError caught")
# except BonusError:
#     print("BonusError caught")


# # --- Cas 2 : Enfant (BonusError) avant le parent (SalaryError)

# print("\nCas 2 : Enfant avant parent")
# emp = Employee("Katze Rik", 50000)
# try:
#     emp.give_bonus(7000)   # Déclenche BonusError
# except BonusError:
#     print("BonusError caught")
# except SalaryError:
#     print("SalaryError caught")

class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()





# perso=Person("Youssef",21)
# perso_2=Person("Youssef",33)
# print(perso_2)
# print(perso) 
# print(perso==perso_2)
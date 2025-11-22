class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"{self.name} est d'age de {self.age} ans "
    def __eq__(self,other):
        return (self.name==other.name and self.age==other.age) 


perso=Person("Youssef",21)
perso_2=Person("Youssef",33)
print(perso_2)
print(perso) 
print(perso==perso_2)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"{self.name} est d'age de {self.age} ans "
    

pesro_1=Person("youssef",21)
print(pesro_1) 
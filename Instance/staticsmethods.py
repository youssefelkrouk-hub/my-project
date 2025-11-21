class Math:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def multiply(x,y):
        return x*y
    @staticmethod
    def add5(x):
        return x+5
    @staticmethod
    def add10(x):
        return x+10
    @staticmethod
    def PI():
        return 3.14159 

class Pizza:
    def __init__(self,radius,ingredients):
        self.radius=radius 
        self.ingredients=ingredients
    def __str__(self):
        return f" ingredients of this pizza type are : {', '.join(self.ingredients)}"
    def area(self):
        return Pizza.circle_area(self.radius)
    @staticmethod
    def circle_area(r):
        return Math.PI() * (r**2) 

p=Pizza(5, ['cheese','salate','pepperoni'])
print(p.area()) 
print(Pizza.circle_area(5)) 


#static method  n'agit pas ni  sur l'attribut ni sur la class 














# class Chien:
#     def parler(self):
#         return "Woof!"

# class Chat:
#     def parler(self):
#         return "Miaou!"

# def faire_parler(animal):
#     return animal.parler()

# def type_animal(animal):
#     if faire_parler(animal)=="Woof!":
#         return "C'est un chien"
#     else:
#         return "C'est un chat"
# # Utilisation
# print(faire_parler(Chien()))
# print(type_animal(Chat()))
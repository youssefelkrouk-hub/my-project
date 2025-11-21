import time
class Student:
    #class attribute
    no_of_students=0
    def __init__(self,name,age,shool_name): #on ajouter default values  
        # instance attributes
        self.__name=name #private attribute
        self.__age=age #private attribute
        self.__school_name=shool_name #private attribute tow inderscores __
        Student.no_of_students += 1 #c'est pourqoui on utilise Student.no_of_students#  
    def describe(self):
        return f"My name is {self.__name} and I am {self.__age} years old ." 
    def get (self):
        return  self.__school_name 
    @classmethod
    def initFromBirthday(cls,name, year_of_birth,school_name):
        current_year=time.localtime().tm_year
        age=current_year - year_of_birth
        return cls(name,age, school_name)
    @classmethod
    def info(cls,name , age,school_name):
        school=school_name.upper()
        return cls(name,age, school)
    







class Pizza:
    def __init__(self,ingredients):
        self.ingredients=ingredients
    def afficher_ingredients(self):
        return f" ingredients of this pizza type are : {', '.join(self.ingredients)}"
    @classmethod
    def veg(cls):
        return cls(['mushrooms','peppers','onions'])
    @classmethod
    def margharite(cls):
        return cls(['mozzarella','tomatoes','saude'])
    def __str__(self):
        return f" ingredients of this pizza type are : {', '.join(self.ingredients)}"

    
pizza = Pizza(['cheese','salate','pepperoni'])
pizza1=Pizza.veg()
pizza2=Pizza.margharite()
print(pizza,pizza1,pizza2,sep="\n")
print("affichage sans dunder function : ")
print(pizza.afficher_ingredients(),pizza1.afficher_ingredients(),pizza2.afficher_ingredients(),sep="\n")








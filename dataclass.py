#sans data class la creation d'un  classe se fait 

# class Person:
#     def __init__(self, name, age, courses):
#         self.name = name
#         self.age = age
#         self.courses = courses
    
#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age}, courses={self.courses})"
#     # on va definir la fonction qui fait l'egalité entre les 2 #
#     def __eq__(self, other):
#         t=(self.name,self.age,self.courses)
#         y=(other.name,other.age,other.courses)
#         return t==y


    

# personne1=Person("Hamada",30,"Ysfàgmail.com")
# personne2=Person("Hamada",30,"Ysfàgmail.com")

# print(personne1)  #pour dataclass cette appel permet de faire , ce que fait la onction __repr__ sans dataclass  
# print(personne2)
# print(personne1==personne2) #print(id(personne1)==id(personne2)) :  retourn false sans dataclass les deux instance n'ont pas les memes id ie il compare les id et n'ont pas le contenu  # 
# #ici aprés la définition de equal (sans data class) selon les attributs # 

#========================================================================================================================




from dataclasses import dataclass , field 
@dataclass(order=True)  # decroters 
class Person():
    name:str   #je peut ajouter default values # 
    age:int 
    email:str 
    # def __eq__(self, other):
    #     t=(self.age)
    #     y=(other.age)
    #      #on commpare selon l'age
    #     return t==y   
    def __post__init__(self):
        self.sort.index =  self.age

personne1=Person("Hamada ",30,"Ysfàgmail.com")
personne2=Person("Hamada",30,"Ysfàgmail.com")
print(personne1==personne2)

import pytest  
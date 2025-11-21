class Student:
    #class attribute
    no_of_students=0
    def __init__(self,name,age,courses): #on ajouter default values  
        # instance attributes
        self.__name=name #private attribute
        self.__age=age #private attribute
        self.__courses=courses #private attribute tow inderscores __
        Student.no_of_students += 1 #c'est pourqoui on utilise Student.no_of_students#  
    def get (self):
        return self.__name ,self.__age,self.__courses
    def set(self,new_name,new_age,new_courses):
        self.__name=new_name
        self.__age=new_age
        self.__courses=new_courses

    def describe(self):
        return f"My name is {self.__name} and I am {self.__age} years old ,I studying {", ".join(self.__courses)}." 
    

student_1=Student("Youssef",34,['CS','Math','Physics'])
print(student_1.get()) 
#print(student_1._Student__age)    (# accessing private attribute using name mangling)  
student_1.set("Ali",22,["Biology","Chemistry"])
print("aprés modification par la fonction set :")
print(student_1.get())
#print(student_1._Student__age)  (# accessing private attribute using name mangling)   
student_1.name="Mouad"
print(student_1.name) #il va afficher moaud mais dans ce cas on n'a pas modifier dans le private attribute __name mais on a cree une autre # 

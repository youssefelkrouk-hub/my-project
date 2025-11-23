
# class employe:
#     #define a class attribute on peut l'utiliser pour  
#     # Minsalary=5000
#     def __init__(self,name,salary,):
#         #define an instance 
#         self.name=name
#         #use class name to access to class attribute
#         self.salary=salary
#     @classmethod
#     def Myclass(cls,name,salary):
#         ssl=salary/2
#         return cls(name,ssl)


# from datetime import datetime

# class BetterDate:
#     def __init__(self, year, month, day):
#         self.year, self.month, self.day = year, month, day
      
#     @classmethod
#     def from_str(cls, datestr):
#         year, month, day = map(int, datestr.split("-"))
#         return cls(year, month, day)
      
#     @classmethod
#     def from_datetime(cls):   # correction ici
#         return cls(datetime().year, datetime().month, datetime().day)

# # Test 
# today = datetime.today()     
# bd = BetterDate.from_datetime(today)   
# print(bd.year)   # affiche l'année actuelle
# print(bd.month)  # affiche le mois actuel
# print(bd.day)    # affiche le jour actuel
#la class qui cree chaque noeud #


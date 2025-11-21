class Pizza:
    def __init__(self,durré, ingredients):
        self.__durré=durré
        self.__ingredients=ingredients
    def afficher_ingredients(self):
        return f" ingredients of this pizza type are : {', '.join(self.ingredients)}"
    def get(self):
        return self.__durré
    def __str__(self):
        return f"{self.__durré} et les ingredients sont {self.__ingredients}" 
    def __add__(self,other):
        nouveau_durre=self.__durré + other.__durré
        return Pizza(nouveau_durre,self.__ingredients)
    def __iadd__(self,other):
        nouveau_durre=self.__durré + other.__durré  
        return Pizza(nouveau_durre,self.__ingredients)
    
pizza1 = Pizza(33, ["tomato", "ketchup"])
pizza2 = Pizza(33, ["cheese", "onion"])
# pizza1+=pizza2 
pizza2+=pizza1
print(pizza2)
pizza2=pizza2+pizza1 #ici on modeffier dans le nouveau pizza2 creé  ie pizza2=66 # 
print(pizza2.get())
print(pizza2)




#{self.__class__.__name__} permet de retourner le nom de la class 








# Classe de base (parent),parent class for etudiant and teacher
#inhertance is usfeful to avoid code duplication or DRY (Don't Repeat Yourself)
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom}, j'ai {self.age} ans."
# Classe dérivée (enfant) qui hérite de Personne , or child class 
class Etudiant(Personne):
    def __init__(self, nom, age, filiere):
        # On réutilise le constructeur de Personne avec super() exempel: super().__init__(nom, age) 
        Personne.__init__(self,nom, age)
        # en genéral on utilise : classpére.__init__(self,par1,pra2,..)
        self.filiere = filiere
    # Redéfinition (override) de la méthode se_presenter
    def se_presenter(self):
        return f"{super().se_presenter()} Je suis étudiant en {self.filiere}."
class Teacher(Personne):
    def __init__(self, nom, age, subject):
        # On réutilise le constructeur de Personne avec super()  
        Personne.__init__(self, nom, age)
        #ou utiliser super().__init__(nom, age) 
        self.subject = subject
    
    # Redéfinition (override) de la méthode se_presenter
    def se_presenter(self):
        return f"{super().se_presenter()} Je suis enseigant  en {self.subject}."

# Utilisation des classes 
p = Personne("Alice", 30)
e = Etudiant("Youssef", 22, "Informatique")
t=Teacher("Dr. Smith", 45, "Mathématiques")
print(p.se_presenter())  # Je m'appelle Alice, j'ai 30 ans.
print(e.se_presenter())  # Je m'appelle Youssef, j'ai 22 ans. Je suis étudiant en Informatique.
print(t.se_presenter())  # Je m'appelle Dr. Smith, j'ai 45 ans. Je suis enseigant en Mathématiques.

import numpy as np
import matplotlib.pyplot as plt
#creation d'une classe matiere # 
class matiere:
    #definition du constructeur
    def __init__(self,nom_matiere,coef,notes):
        self.nom_matiere=nom_matiere
        self.coef=coef
        self.notes=notes
    # Méthode (comportement de l'objet)
    def moyenne(self):
        t=np.mean(self.notes)
        return t
    # Méthode (comportement de l'objet)
    def afficher_matiere(self):
        return f"la matiere {self.nom_matiere} a pour coefficient {self.coef} et la moyenne est {self.moyenne()}."
    

# #creation d'une classe etudiant
class etudiant:
    #definition du constructeur
    def __init__(self,nom,prenom,age,filiere):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.filiere=filiere 
    ## Méthode (comportement de l'objet)
    def sepresenter(self):
        return f"je m'appelle {self.prenom} {self.nom} j'ai {self.age} ans et je ma filiere est {self.filiere}."
# Création d'objets (instances de la classe)
# etd = etudiant("Youssef","haha",22,"ISI")
# print(etd.nom) # Accès à un attribut 
# print(etd.prenom)
# print(etd.age)
# print(etd.sepresenter()) # Appel d'une méthode de l'objet






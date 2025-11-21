from OOP import *   
# Création d'instances de la classe etudiant c'est à dire des objets c'est l'instanciation de la classe
# etd=etudiant("Youssef","haha",22,"data scientist")
# etd2=etudiant("Ali","mdr",21,"ISI")
# print(etd.nom) # Accès à un attribut
# print(etd.prenom)
# print(etd.age)
# print(etd.filiere)

# print("\nPrésentation de l'étudiant :\n")
# print(etd.sepresenter())
# print("\nPrésentation de l'étudiant 2:\n")
# print(etd2.sepresenter())
# print("\n---------------------------------\n")
from exe import subject as Matiere 
from Oct import Profile
# Création d'instances de la classe etudiant c'est à dire des objets c'est l'instanciation de la classe matiere 
print("\nCréation des matières:\n")
matiere1=Matiere("maths",14,[12,13,15,16]) # Création d'une instance de la classe matiere
print("\nDétails de la matière 1:\n")
print(matiere1.nom_matiere)
print(matiere1.coef)
print(matiere1.notes)
print(matiere1.moyenne())
print(matiere1.afficher_matiere())
print(matiere1.trier_matiere())

matiere2=Matiere("physique",12,[10,11,14,13]) # Création d'une instance de la classe matiere 

print("\nDétails de la matière 2:\n")
print(matiere2.nom_matiere)
print(matiere2.coef)
print(matiere2.notes)
print(matiere2.moyenne())
print(matiere2.afficher_matiere())
print(matiere2.trier_matiere())
print("\nAffichage des notes de la matière 1:\n")
matiere1.plot()
print("\nAffichage des notes de la matière 2:\n")
matiere2.plot()




import numpy as np 
import matplotlib.pyplot as plt

class subject:
    # definition du constructeur,deconstructeur est noté par # 
    def __init__(self,nom_matiere,coef,notes):
        self.nom_matiere=nom_matiere
        self.coef=coef
        self.notes=notes
    # Méthode (comportement de l'objet)
    def moyenne(self):
        u=np.mean(self.notes)
        return u
    # Méthode (comportement de l'objet)
    def afficher_matiere(self):
        return f"la matiere {self.nom_matiere} a pour coefficient {self.coef} et la moyenne est {self.moyenne()}."
        # Méthode (comportement de l'objet)
    def trier_matiere(self):
        L=sorted(self.notes,reverse=False)
        return L 
    def plot(self):
        plt.plot(self.notes, marker='o')
        plt.title(f'Notes for {self.nom_matiere}')
        plt.xlabel('Exam Number')
        plt.ylabel('Note')
        plt.grid(True)
        plt.show() 






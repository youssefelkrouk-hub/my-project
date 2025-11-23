

#============LinkedList=============#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_begining(self):
        if self.head is None:
            return None
        #sauvegarder l'ancien head 
        removed_node = self.head
        #deplacer head vers le prochain noeud
        self.head=self.head.next
        if self.head is None:
            self.tail = None
        return removed_node.data
    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head==self.tail:
            removed_node=self.head
            self.head=None 
            self.tail=None
            return removed_node.data
        current=self.head
        #la boucle while permet de determiner l'avant dernier #
        while current.next!=self.tail:
            current=current.next  #
        removed_node=self.tail  
        self.tail=current  #le dernier devient l'avant dernier
        self.tail.next=None  #le next de l'avant dernier 
        return removed_node.data  
    def insert_at_end(self,data):
        new_node=Node(data)    # 1. Créer un nouveau nœud avec la donnée
        if self.head:           #2. vérifier si la liste n’est pas vide
            self.tail.next  = new_node #3. le dernier devient le new_node
            self.tail=new_node          # 4. Mettre à jour tail → le nouveau nœud devient le dernier
        else:  #5.si la liste est vide 
            self.head = new_node        # head et tail pointent tous les deux sur ce nœud
            self.tail = new_node
    def search(self,data):
        current_node=self.head  #on sauvgarde la tete pour parcourir LinkedList
        while current_node:
            if current_node.data==data:
                return True
            current_node=current_node.next
        return False 

# Créer une liste vide
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)


# Afficher la liste
ll.display()
print("la taille est : ")
print("apres suppresion au debut on  obtient") 
ll.remove_at_begining()
ll.display()
print("aprés suppresion a la fin : ")
ll.remove_at_end()
ll.display()
print(ll.search(10))


print("=====Working With Stacks===========")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # par défaut, un nouveau nœud ne pointe vers rien

class Stack:
    def __init__(self):
        self.top = None   # sommet de la pile
        self.size = 0     # taille de la pile

    def push(self, data):
        # Créer un nouveau nœud
        new_node = Node(data)
        # Si la pile n'est pas vide, relier le nouveau nœud à l'ancien sommet
        if self.top:
            new_node.next = self.top
        # Mettre à jour le sommet
        self.top = new_node
        # Incrémenter la taille
        self.size += 1
    def pop(self):
     # Vérifier si la pile est vide (aucun élément au sommet)
     if self.top is None:
         return None   # Rien à retirer, on retourne None
     else:
        # Sauvegarder le nœud actuel au sommet (celui qu'on va retirer)
        popped_node = self.top

        # Décrémenter la taille de la pile car on enlève un élément
        self.size -= 1

        # Mettre à jour le sommet : le nouveau top devient l'élément suivant
        self.top = self.top.next

        # Couper le lien du nœud retiré (bonne pratique pour éviter des références inutiles)
        popped_node.next = None

        # Retourner la donnée contenue dans le nœud retiré
        return popped_node.data



    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(100)
s.display()   # Résultat: 30 -> 20 -> 10 -> None
print("Taille:", s.size)  # 3
#🎯 Conclusion

#Les deux opérations push et pop sont très efficaces : elles s’exécutent en temps constant. 
# C’est ce qui rend la structure stack idéale pour des applications comme :
#gestion du call stack (pile d’appels de fonctions),
#annuler/rétablir (Undo/Redo),
#parcours en profondeur (DFS).


# Import the module to work with Python's LifoQueue
from queue import LifoQueue

# Create an infinite LifoQueue (maxsize=0 = infini)
my_book_stack = LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")
print("My book is ",my_book_stack.queue)
# Remove an element from the stack
my_book_stack.get()

















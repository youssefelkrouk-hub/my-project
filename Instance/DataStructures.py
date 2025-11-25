

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
my_book_stack.put("Aljaber w Almo9abala ")
print("My book is ",my_book_stack.queue)
# Remove an element from the stack
print("aprés la suppresion  : \n ")
my_book_stack.get() #suppresion  au debut (FIFO=First IN First Out)
print(my_book_stack.queue)
print(my_book_stack.empty()) # retourne si queue est vide ou non  #



from queue import Queue
class Printer:
    def __init__(self):
        # Créer une file d’attente
        self.queue = Queue()
    def add_document(self, document):
        # Ajouter un document dans la file
        self.queue.put(document) #on peut utiliser put
    def print_documents(self):
        # Tant qu’il reste des documents dans la file ,is file is not Null
        while not self.queue.empty():
            # Retirer le document de la file et l’imprimer
            print(self.queue.get()) #on peut utiliser .get()


printer = Printer()
printer.add_document("Youssef El krouk ")
printer.add_document("Mouad Belhass")
printer.print_documents()

# print("File vide ?", printer.queue.empty())  # True

# printer.add_document("Doc1")
# print("File vide ?", printer.queue.empty())  # False

# printer.print_documents()
# print("File vide ?", printer.queue.empty())  # True

# Classe Queue simplifiée

class Queue:
    def __init__(self):
        self.items = []
        self.head = None

    def enqueue(self, data):
        # Ajouter un élément à la fin
        self.items.append(data)
        if not self.head:
            self.head = data

    def dequeue(self):
        # Retirer le premier élément (FIFO)
        if self.has_elements():
            removed = self.items.pop(0)
            # Mettre à jour le head
            self.head = self.items[0] if self.items else None
            return removed
        return None

    def has_elements(self):
        # Vérifie si la file contient des éléments
        return self.head is not None 

# Classe PrinterTasks
class Printertalks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        # Ajouter un document à la file
        self.queue.enqueue(document)

    def print_documents(self):
        # Imprimer tous les documents tant que la file n'est pas vide
        while self.queue.has_elements():
            print("Printing", self.queue.dequeue())

printer = Printertalks()
printer.add_document("Youssef El krouk ")
printer.add_document("Mouad Belhass")
printer.print_documents()





from queue import SimpleQueue

# Créez la file d'attente.
my_orders_queue = SimpleQueue()

# Ajouter un élément à la file d'attente.
my_orders_queue.put("Commande 1: Pizza")

# Retirer un élément de la file d'attente.
order = my_orders_queue.get()
print(order)


from queue import Queue

q = Queue(maxsize=2)
q.put("A")
q.put("B")
print(q.get())  # A
#====== La biblio SimpleQueue est plus restrient que queue ============#
from queue import SimpleQueue
sq = SimpleQueue()
sq.put("A")
sq.put("B")
print(sq.get())  # A

print("================ Graphs Impelimentation  =======================\n")

    
class Graph:
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex):
        self.vertices[vertex]=[]
    def  add_edge(self, source, *args):
        self.vertices[source].append(args)
    def display(self):
        for key,value in self.vertices.items():
            for t in value:
                print(f"les amis proche de {key} sont {t}")



my_graph = Graph() 
my_graph.add_vertex('David') 
my_graph.add_vertex('Miriam') 
my_graph.add_vertex('Martin') 
my_graph.add_edge('David', 'Miriam','Youssef','Ilham') 
my_graph.add_edge('Miriam','HHHH')
my_graph.add_edge('Miriam', 'Martin') 
my_graph.add_edge('Martin','Emly')
print(my_graph.vertices)
my_graph.display()

print("======================== Recursion ========================")


#par  memoisation 
cache = [None]*(100)
def fibonacci(n): 
    if n <= 1:
        return n
    # Check if the value exists
    if cache[n] is None:
        # Save the result in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]
    
print(fibonacci(3))

print("================== Tour de Hanoi ==========================")

def hanoi(nb_disques, source, destination, intermediaire):
    # Cas de base : un seul disque
    if nb_disques == 1:
        print(f"Déplacer le disque 1 de {source} vers {destination}")
        return
    # Déplacer n-1 disques vers la tige intermédiaire
    hanoi(nb_disques - 1, source, intermediaire, destination)
    # Déplacer le disque restant vers la tige destination
    print(f"Déplacer le disque {nb_disques} de {source} vers {destination}")
    # Déplacer les n-1 disques de la tige intermédiaire vers la tige destination
    hanoi(nb_disques - 1, intermediaire, destination, source)

# Exemple
nb_disques = 4
source = 'A'
intermediaire = 'B'
destination = 'C'
hanoi(nb_disques, source, destination, intermediaire)



print("===============Binary Search iterative  de complexité logarithmique O(log(x))==============")
def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1
    
    while first <= last:
        middle = (first + last) // 2
        # Vérifier si la valeur recherchée est au milieu
        if search_value == ordered_list[middle]:
            return True
        # Vérifier si la valeur recherchée est plus petite que celle au milieu
        elif search_value < ordered_list[middle]:
            # Réduire la borne supérieure
            last = middle - 1
        else:
            # Augmenter la borne inférieure
            first = middle + 1
    return False

print(binary_search([1, 5, 8, 9, 15, 20, 70, 72], 5))  # Résultat attendu : True

print("===============Binary Search Recurrsive==============")

def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[middle+1:],search_value) 
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))

print("Depth-First Search (DFS) : Parcours en profondeur d'un graphe")











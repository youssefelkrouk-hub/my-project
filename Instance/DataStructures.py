class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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

    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")
    def insert_at_end(self,data):
        new_node=Node(data)    # 1. Créer un nouveau nœud avec la donnée
        if self.head:           #2. vérifier si la liste n’est pas vide
            self.tail.next  = new_node #3. le dernier devient le new_node
            self.tail=new_node          # 4. Mettre à jour tail → le nouveau nœud devient le dernier
        else: #5.si la liste est vide 
            self.head = new_node        # head et tail pointent tous les deux sur ce nœud
            self.tail = new_node


# Créer une liste vide
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(55)
# Afficher la liste
ll.display()
print("apres suppresion au debut on  obtient") 
ll.remove_at_begining()
ll.display()
print("aprés suppresion a la fin : \n")
ll.remove_at_end()
ll.display()
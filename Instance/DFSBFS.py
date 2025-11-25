# class TreeNode:
#     def __init__(self, data,left=None,right=None):
#         self.data= data
#         self.left = left
#         self.right = right

   
# #la class qui cree chaque noeud #
# class GraphNode:
#     def __init__(self, data):
#         self.data = data
#         self.adjacent = []  # liste des noeuds adjacents    
#     def add_edge(self, neighbor_node):
#         self.adjacent.append(neighbor_node)
# #la class qui cree le graphe#
# class Graph:
#     def __init__(self):
#         self.vertices = []  # liste des noeuds du graphe    
#     def add_vertex(self, node):
#         self.vertices.append(node)  
#     def display(self):
#         for vertex in self.vertices:
#             edges = [neighbor.data for neighbor in vertex.adjacent]
#             print(f"{vertex.data} --> {', '.join(map(str, edges))}")
# # Exemple d'utilisation
# my_graph = Graph()  
# nodeA = GraphNode('A')
# nodeB = GraphNode('B')
# nodeC = GraphNode('C')
# nodeD = GraphNode('D')
# my_graph.add_vertex(nodeA)
# my_graph.add_vertex(nodeB)
# my_graph.add_vertex(nodeC)
# my_graph.add_vertex(nodeD)
# nodeA.add_edge(nodeB)
# nodeA.add_edge(nodeC)
# nodeB.add_edge(nodeD)
# nodeC.add_edge(nodeD)
# print("=============== Graph Representation ===============")
# my_graph.display()

class TreeNode:
    def __init__(self, data,left=None,right=None):
        self.data= data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self): 
        self.root = None

print("algorithme of searching in a binary search tree")
#a binary search tree (BST) is a node-based binary tree data structure which has the following properties:
# The left subtree of a node contains only nodes with keys less than the node's key. partie gauche<noeud
# The right subtree of a node contains only nodes with keys greater than the node's key. partie droite>noeud
# The left and right subtree each must also be a binary search tree.

def Searche(self,search_value):
    current_node = self.root
    while current_node:
        if search_value == current_node.data:
            return True  # Valeur trouvée
        elif search_value < current_node.data:
            current_node = current_node.left  # Aller à gauche
        else:
            current_node = current_node.right  # Aller à droite
    return False  # Valeur non trouvée
# class BinarySearchTree:
#   def __init__(self):
#     self.root = None

#   def insert(self, data):
#     new_node = TreeNode(data)
#     # Check if the BST is empty
#     if self.root == None:
#       self.root = new_node
#       return
#     else:
#       current_node = self.root
#       while True:
#         # Check if the data to insert is smaller than the current node's data
#         if data < current_node.data:
#           if current_node.left_child == None:
#             current_node.left_child = new_node
#             return 
#           else:
#             current_node = current_node.left_child
#         # Check if the data to insert is greater than the current node's data
#         elif data > current_node.data:
#           if current_node.right_child == None:
#             current_node.right_child = new_node
#             return
#           else:
#             current_node = current_node.right_child

# bst = TreeNode()
# bst.insert("Pride and Prejudice")
# print(Searche(bst, "Pride and Prejudice"))

# Exemple d'utilisation
# bst = BinarySearchTree()
# bst.root = TreeNode(10)
# bst.root.left = TreeNode(5)
# bst.root.right = TreeNode(15)
# bst.root.left.left = TreeNode(3)
# bst.root.left.right = TreeNode(7)
# bst.root.right.right = TreeNode(20)
# print("Searching for 7 in the BST:", Searche(bst, 7))  # Output: True


print("Finding Minimum and Maximum in a Binary Search Tree")
class TreeNode:
    def __init__(self, data,left_child=None,right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find_min(self):
        # Définir current_node comme la racine
        current_node = self.root
        # Parcourir jusqu'au nœud le plus à gauche
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data
    def find_max(self):
        cr=self.root
        while cr.right_child :
            cr=cr.right_child
        return cr.data

# Exemple : création d'un arbre
def CreateTree():
    bst = BinarySearchTree()
    bst.root = TreeNode(50)
    bst.root.left_child = TreeNode(30)
    bst.root.right_child = TreeNode(70)
    bst.root.left_child.left_child = TreeNode(20)
    bst.root.left_child.right_child = TreeNode(40)
    bst.root.right_child.left_child = TreeNode(60)
    bst.root.right_child.right_child = TreeNode(1000)
    return bst

bst = CreateTree()
print(bst.find_min())  # Résultat attendu : 20
print(bst.find_max())  # Résultat attendu : 80


print("In-Order Traversal of a Binary Search Tree\n")

class TreeNode:  
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order(self, current_node):
        # Vérifier si le nœud existe
        if current_node:
            # Parcourir récursivement le sous-arbre gauche
            self.in_order(current_node.left_child)
            
            # Afficher la valeur du nœud courant
            print(current_node.data)
    
            # Parcourir récursivement le sous-arbre droit
            self.in_order(current_node.right_child)
    def in_desorde(self,current_node):
        if current_node:
            #parcourir le sous arbre droite
            self.in_desorde(current_node.right_child)
            print(current_node.data)
            self.in_desorde(current_node.left_child)

    @staticmethod
    def CreateTree():
        bst = BinarySearchTree()
        bst.root = TreeNode(50)
        bst.root.left_child = TreeNode(30)
        bst.root.right_child = TreeNode(70)
        bst.root.left_child.left_child = TreeNode(20)
        bst.root.left_child.right_child = TreeNode(40)
        bst.root.right_child.left_child = TreeNode(60)
        bst.root.right_child.right_child = TreeNode(1000)
        return bst

#creation
bst = CreateTree()

# Parcours en ordre
bst.in_order(bst.root)
print("In-Desorder Traversal of a Binary Search Tree")
bst.in_desorde(bst.root)

print("Pre-Order Traversal of an Expression Tree\n")


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class ExpressionTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current_node):
        # Vérifier si le nœud existe
        if current_node:
            # Afficher la valeur du nœud courant
            print(current_node.data)
            # Appeler récursivement sur le sous-arbre gauche
            self.pre_order(current_node.left_child)
            # Appeler récursivement sur le sous-arbre droit
            self.pre_order(current_node.right_child)


# Exemple : construire un petit arbre d'expression
def CreateExpressionTree():
    # Expression : (A + B) * C
    nodeA = TreeNode("A")
    nodeB = TreeNode("B")
    nodeC = TreeNode("C")
    plus = TreeNode("+", nodeA, nodeB)
    multiply = TreeNode("*", plus, nodeC)

    et = ExpressionTree()
    et.root = multiply
    return et


# Test
et = CreateExpressionTree()
et.pre_order(et.root)

print("Depth-First Search (DFS) : Parcours en profondeur d'un graphe")
#version recurssive 
def dfs_recu(visited_vertices, graph, current_vertex):
    # Vérifier si le sommet n'a pas encore été visité
    if current_vertex not in visited_vertices:
        print(current_vertex)  # Afficher le sommet
        visited_vertices.add(current_vertex)  # Marquer comme visité
        # Explorer tous les voisins
        for adjacent_vertex in graph[current_vertex]:
            dfs_recu(visited_vertices, graph, adjacent_vertex)

#version iterative en utilisant une pile
def dfs_iterative(graph, start_vertex):
    visited_vertices = set()
    stack = [start_vertex]

    while len(stack) > 0: # Tant que la pile n'est pas vide ou on peut aussi utiliser while stack:
        current_vertex = stack.pop()  # Retirer le sommet du haut de la pile et le sauvegarder dans current_vertex
        # Vérifier si le sommet n'a pas encore été visité
        if current_vertex not in visited_vertices: # Si non visité
            print(current_vertex) # Afficher le sommet
            visited_vertices.add(current_vertex)# Marquer comme visité
            # Ajouter les voisins dans la pile
            # (on inverse pour garder un ordre similaire au récursif)
            for adjacent_vertex in graph[current_vertex]:
                if adjacent_vertex not in visited_vertices:
                    stack.append(adjacent_vertex)

# Exemple de graphe sous forme de dictionnaire d'adjacence
graph = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0', '5'],
    '3': ['1'],
    '4': ['1', '5'],
    '5': ['2', '4']
}
print("avec une liste, la vérification not in est O(n) au lieu de O(1) avec un set. Donc en pratique, un set est plus efficace.")
# Test récursif
print("DFS récursif :")
dfs_recu(set(), graph, '0')
print("DFS iterative:")
dfs_iterative(graph, '0')

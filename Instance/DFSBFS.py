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



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

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

# Exemple : création d'un arbre
def CreateTree():
    bst = BinarySearchTree()
    bst.root = TreeNode(50)
    bst.root.left_child = TreeNode(30)
    bst.root.right_child = TreeNode(70)
    bst.root.left_child.left_child = TreeNode(20)
    bst.root.left_child.right_child = TreeNode(40)
    bst.root.right_child.left_child = TreeNode(60)
    bst.root.right_child.right_child = TreeNode(80)
    return bst

bst = CreateTree()
print(bst.find_min())  # Résultat attendu : 20

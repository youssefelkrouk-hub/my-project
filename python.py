
import numpy as np 
import matplotlib.pyplot as plt        
A = np.array([[2, 1, 1],
              [4, 3, 3],
              [8, 7, 9]])
B=np.linalg.svd(A)
U,B1,Vt=B
print("matrice U S Vt \n")
print(U)
print(B1)
print(Vt)
print("reconstruction de la matrice A \n")
S=np.zeros((3,3))
for i in range(3):
    S[i][i]=B1[i]
A_reconstructed=U@S@Vt
print(A_reconstructed)
print("\n")


print()

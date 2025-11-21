import numpy as np


# todo : algorithme de resolution d'n systéme linaire : 
def resotriang(A,b):
    #! la matrice A est traingulaire supérieure(elemination de gauss)
    n=len(A)
    x=[0]*n
    x[n-1]=b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s=0
        for k in range(i+1,n):
            s=s+A[i][k]*x[k]
        x[i]=(b[i]-s)/A[i][i]
    return x


# todo : DEFINIR LE MINEUR(A,i,j): c'est la matrice A en eliminant la i éme ligne et la j émé colonne
def mineur(A,i,j):
    n=len(A)
    mineur=[[A[k][l]for k in range(n) if k!=i] for l in range(n)if l!=j]
    return mineur 
 #! DEFINIR LE DETERMINAT RECURSIVE EN UTILSANT LE MINEUR 

def detrecu( A ) : 
    n=len(A)
    if n==1:
        return A[0]
    if n==2 : 
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    det=0
    for j in range(n):

        det+=((-1)**j)*A[0][j]*detrecu(mineur(A,0,j))


    return det 

def produitscalaire(v1,v2):
    return np.dot(v1,v2)
 
def decompQR1(A):
    n=len(A)
    if (detrecu(A)==0):
        return None
    Q=np.zeros((n,n))  #! A=QR donc il suffit de calculer Q car R=Q.T@A
    
    for i in range(n):
        U=A[ :,i].copy()
        for k in range(i):
            coef= np.dot(Q[:,k],A[:,i])
            U = U -coef*Q[:,k]
        Q[:,i]=U/np.linalg.norm(U)
    R=Q.T@A
   
    return Q 

def decompQR2(A):
    n=len(A)
    Q=np.zeros((n,n))
    R=np.zeros((n,n))
    for i in range(n):
        v=A[ :,i].copy()
        for k in range(i):
            R[k,i]=np.dot(A[:,i],Q[:,k])
            v=v-R[k,i]*Q[:,k]
        R[i,i]=np.linalg.norm(v)
        Q[:,i]=v/R[i,i]
    return Q,R,Q@R

        

def chelosky1(S):
    n=len(S)
    T=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i):
                s+=T[i][k]*T[j][k]
            if i==j:
                T[i][i]=(S[i][i]-s)**(1/2)
            else:
                T[j][i]=(S[i][j]-s)/T[i][i]
    return T


def chelosky2(S):
    n=len(S)
    L=np.zeros((n,n))
    L[0][0]=S[0][0]**0.5
    for j in range(1,n):
        L[j][0]=S[j][0]/L[0][0]
    for i in range(1,n):
        s=0
        for k in range(0,i):
            s=s+(L[i][k]**2)
        L[i][i]=(S[i][i]-s)**0.5

        for j in range(i+1,n):
           h=0
           for k in range(i):
               h=h+L[j][k]*L[i][k]
    return L
def dg(A):
    n=len(A)
    D=np.zeros((n,n))
    for i in range(n):
        D[i][i]=A[i][i]
    return D
def eg(A):
    n=len(A)
    E=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i>j:E[i][j]=-A[i][j]
            #! il ya une fonction predefinie   :  
            #? np.tril(A,+1) 

    return E

def fg(A):
    n=len(A)
    F=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i<j:F[i][j]=-A[i][j]
            #! il ya une fonction predefinie  :  
            #? np.triu(A,-1) 
    return F

#!on verifion

def est_strdominante(A):
    n=len(A)
    for i in range(n):
        s=0
        for j in range(n):
            if j!=i:
                s+=abs(A[i][j])
        if s<abs(A[i][i]): return False
    return True



def methodejacoubi(A,b,x,epsilon):
    #! on decompose A en A=D-E-F ##
    #! Dx^(k+1)=(E+F)X^(k)+b pour tout k>=0 avec x(0) une vecteru qlq
    n=len(A)
    D=dg(A)                    #?(returne les elts diagonaux de A sous forme d'un matrice ou utiliser D(A))
    E=eg(A)                       #!-np.tril(A,-1)                                #? -np.tril(A,-1) 
    F=fg(A)                  #!-np.triu(A,1)                                    #? -np.triu(A1)  
    k=0                                         #?nombre d'iteration 
    erreurs=[ ]
    while 2*epsilon>epsilon :                           #? np.triu(A,-1) 
        x=np.dot(np.linalg.inv(D),(np.dot((E+F),x)+b))
        u=np.dot(A,x)
        erreur =np.linalg.norm(u-b)
        erreurs.append(erreur)
        k+=1
        print(k,epsilon,x)
        print("\n")
    return [k,x,erreurs]


#! La methode de gauss seidel #!
def methodeGaus_siedel(A,b,x,epsilon):
    #! on decompose A en A=D-E-F ##
    #! (D-E)x^(k+1)=(F)X^(k)+b pour tout k>=0 avec x(0) une vecteru qlq
    n=len(A)
    D=np.diag(np.diag(A))                    #?(returne les elts diagonaux de A sous forme d'un matrice ou utiliser D(A))
    E=-np.tril(A,-1)                               #? -np.tril(A,-1) 
    F=-np.triu(A,1)                                #? -np.triu(A1)  #? np.triu(A,-1)                                        #?nombre d'iteration 
    erreurs = [  ]
    k=0
    while 2*epsilon>epsilon :                           
        x=np.dot(np.linalg.inv(D-E),(np.dot((F),x)+b))
        u=np.dot(A,x)
        erreur=np.linalg.norm(u-b)               #? la méthode converge quand epsilon tend vers 0 #?
        erreurs .append(erreur)
        k+=1
        print(k,epsilon,x)
        print("\n")
    return [k,x,erreurs]  




A = np.array([[1, 2, 1],
              [2, 3, 4],
              [1,4, -4]],dtype=float)

B=np.linalg.cholesky(A@A.T)
H=A@A.T
print(H)
print(B)


K=np.array([[0, -1, 1],
              [1, 0, 2],
              [0,0, 3]],dtype=float)

t=np.linalg.qr(K)
Q,R=np.linalg.qr(K)
print("Q:",Q)
print("R:",R)
print("QR:",Q@R)
print("detrecu:",np.linalg.det(K))










    



    

    






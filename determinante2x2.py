#Una función humilde para obtener el determinante de una matriz de 2x2.

import numpy as np

def det2x2 (A):
    """
    El parámetro A es nuestra matriz 2x2 de la cual buscamos su determinante
    """
    if (A.shape==(2,2)):
        detA=A[0,0]*A[1,1]-A[0,1]*A[1,0]
        print (detA)
    else:
        print ("La matriz no es de 2x2")

#Podemos ver un ejemplo con la matriz B:
B=np.array([[2,1],
            [7,2]])

detB=det2x2(B)

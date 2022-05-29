from LU.LU_decomposition import LU_decomposition
from Gauss_Jacobi.gauss_jacobi import Gauss_Jacobi

if __name__ == '__main__':
    #Test
    A = [[3, 2, 4],
          [1, 1, 2],
          [4, 3, -2]]

    b = [1, 2, 3]

    LU_decomposition = LU_decomposition(A, b)
    print(LU_decomposition.solve())

    A = [[10, 2, 1],
         [1, 5, 1],
         [2, 3, 10]]

    b = [7, -8, 6]
    Gauss_Jacobi = Gauss_Jacobi(A, b, 0.01)
    print(Gauss_Jacobi.solve())



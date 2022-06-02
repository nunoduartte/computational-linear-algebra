from LU.LU_decomposition import LU_decomposition
from Gauss_Jacobi.gauss_jacobi import Gauss_Jacobi
from Lagrange_Interpolating_Polynomial.lagrange_interpolation import Lagrange_Interpolation
from Jacobi_Method.jacobi_method import Jacobi_Method

if __name__ == '__main__':
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

    x_target = 1.5
    x = [-1, 0, 2, 3]
    y = [4, 1, -1, 4]
    Lagrange_Interpolation = Lagrange_Interpolation(x_target, x, y)
    print(Lagrange_Interpolation.solve())


    matrix = [[3,2,0], [2,3,-1], [0,-1,3]]
    tolerance = 10 ** (-5)
    Jacobi_Method = Jacobi_Method(matrix, tolerance)
    print(Jacobi_Method.solve())




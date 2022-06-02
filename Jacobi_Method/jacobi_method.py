import math
from Matrix_Operations.matrix_operations import Matrix_Operations

class Jacobi_Method:
    def __init__(self, matrix, tolerance):
        self.matrix = matrix
        self.tolerance = tolerance
        self.matrix_operations = Matrix_Operations()

    def solve(self):
        number_of_rows = len(self.matrix)
        eigenvector = [[float(i == j) for i in range(number_of_rows)]
                       for j in range(number_of_rows)]
        highest_value = self.__highest_value(self.matrix)
        number_of_iterations = 1

        while (math.fabs(self.matrix[highest_value[0]][highest_value[1]]) > self.tolerance):
            rotation_matrix = self.__calculate_rotation_matrix(self.matrix, highest_value)
            eigenvector = self.matrix_operations.multiply_matrixes(eigenvector, rotation_matrix)
            rotation_matrix_transposed = self.matrix_operations.calculate_transposed(rotation_matrix)
            self.matrix = self.matrix_operations.multiply_matrixes(rotation_matrix_transposed, self.matrix_operations.multiply_matrixes(self.matrix, rotation_matrix))
            highest_value = self.__highest_value(self.matrix)
            number_of_iterations += 1

        result = []
        for i in range(number_of_rows):
            result.append((i + 1, self.matrix[i][i], eigenvector[i]))
            print(str(i + 1) + "° Eigenvalue: " + str(self.matrix[i][i]) + ", Eigenvector: " + str(eigenvector[i]))
        print("Number of Iterations: " + str(number_of_iterations))

        return result

    def __highest_value(self, matrix_a):
        number_of_rows = len(matrix_a)
        highest = -math.inf
        for i in range(number_of_rows):
            for j in range(number_of_rows):
                if (i != j and math.fabs(matrix_a[i][j]) > highest):
                    highest = math.fabs(matrix_a[i][j])
                    index = (i, j)
        return index

    def __calculate_rotation_matrix(self, matrix, indexes):
        number_of_rows = len(matrix)

        rotation_matrix = [[0.0 for i in range(number_of_rows)]
                    for j in range(number_of_rows)]

        for i in range(number_of_rows):
            rotation_matrix[i][i] = 1.0

        alpha = self.__calculate_alpha(matrix, indexes)

        rotation_matrix[indexes[0]][indexes[0]] = math.cos(alpha)
        rotation_matrix[indexes[1]][indexes[1]] = math.cos(alpha)
        rotation_matrix[indexes[0]][indexes[1]] = -math.sin(alpha)
        rotation_matrix[indexes[1]][indexes[0]] = math.sin(alpha)

        return rotation_matrix

    def __calculate_alpha(self, matrix, indexes):
        denominator = (matrix[indexes[0]][indexes[0]] -
                       matrix[indexes[1]][indexes[1]])

        if (matrix[indexes[0]][indexes[0]] == matrix[indexes[1]][indexes[1]]):
            return math.pi / 4
        else:
            return math.atan(2 * matrix[indexes[0]][indexes[1]] / denominator) / 2
import math

class Gauss_Jacobi:
    def __init__(self, A, b, tolerance):
        self.A = A
        self.b = b
        self.tolerance = tolerance

    def solve(self):
        n = len(self.b)
        x = self.b.copy()

        hasSolution = self.__main_diagonal_is_not_zero(n)
        if hasSolution == False:
            return x

        for i in list(range(0, n)):
            main_diagonal_element = self.A[i][i]
            x[i] = self.b[i] / main_diagonal_element

        next_x_iteration = x.copy()
        current_iteration = 0
        max_iterations = 10

        while(current_iteration < max_iterations):
            current_iteration = current_iteration + 1
            for i in list(range(0, n)):
                sum_line = 0
                for j in list(range(0, n)):
                    if (i != j):
                        sum_line = sum_line + self.A[i][j] * x[j]
                next_x_iteration[i] = (1 / self.A[i][i]) * (self.b[i] - sum_line)

            if self.__compare(x, next_x_iteration):
                x = next_x_iteration.copy()
                break
            x = next_x_iteration.copy()
        return x

    def __main_diagonal_is_not_zero(self, n):
        for i in list(range(0, n)):
            if (math.fabs(self.A[i][i]) == 0):
                return False
        return True

    def __compare(self, x, next_x_iteration):
        biggest_diff = 0
        next_x_biggest_value = 0
        for i in list(range(0, len(x))):
            diff = math.fabs(x[i] - next_x_iteration[i])
            if diff > biggest_diff:
                biggest_diff = diff
            if next_x_iteration[i] > next_x_biggest_value:
                next_x_biggest_value = next_x_iteration[i]

        residual = biggest_diff / next_x_biggest_value
        return residual < self.tolerance


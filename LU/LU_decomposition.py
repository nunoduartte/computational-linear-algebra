class LU_decomposition:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def solve(self):
        self.A = self.__LU(self.A)
        y = self.__solveLower(self.A, self.b)
        x = self.__solveUpper(self.A, y)
        return x

    def __LU(self, A):
        n = len(A)
        x = [0] * n

        # Calculate the pivot
        for k in list(range(1, n)):
            # Calculate the multipliers
            for i in list(range(k, n)):
                current_element = A[i][k - 1]
                pivot = A[k - 1][k - 1]
                multiplier = current_element / pivot
                A[i][k - 1] = multiplier

                # Aply operation to the others elements in the line
                for j in list(range(k, n)):
                    others_elements_pivot = A[k - 1][j]
                    others_elements_current_element = A[i][j]
                    result_operation = others_elements_current_element - multiplier * others_elements_pivot
                    A[i][j] = result_operation

        return A

    def __solveLower(self, L, b):
        n = len(b)
        y = [0] * n

        for i in list(range(0, n)):
            sum_line = 0
            for j in list(range(0, i)):
                current_element_line = L[i][j]
                sum_line = sum_line + current_element_line * y[j]

            y[i] = b[i] - sum_line

        return y

    def __solveUpper(self, U, b):
        n = len(b)
        x = [0] * n
        x[n - 1] = b[n - 1] / U[n - 1][n - 1]

        for i in list(range(n-1, 0, -1)):
            sum_line = 0
            for j in list(range(i + 1, n + 1, 1)):
                sum_line = sum_line + U[i - 1][j - 1] * x[j - 1]

            x[i - 1] = (b[i - 1] - sum_line) / (U[i - 1][i - 1])

        return x
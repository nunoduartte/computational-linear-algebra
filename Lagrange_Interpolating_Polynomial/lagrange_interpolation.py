class Lagrange_Interpolation:
    def __init__(self, x_target, x, y):
        self.x_target = x_target
        self.x = x
        self.y = y

    def solve(self):
        y_target = 0
        degree = 2
        for k in range(0, degree + 1):
            p = 1
            for j in range(0, degree + 1):
                if k != j:
                    p = p * (self.x_target - self.x[j]) / (self.x[k] - self.x[j])

            y_target = y_target + p * self.y[k]
        return y_target
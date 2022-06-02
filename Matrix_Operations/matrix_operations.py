class Matrix_Operations:
    def __init__(self):
        pass

    def calculate_transposed(self, M):
        mTemp = []
        for i in range(len(M[0])):
            temp = []
            for j in range(len(M)):
                temp.append(M[j][i])
            mTemp.append(temp)
        return mTemp

    def multiply_matrixes(self, M, N):
        tempM = []
        for i in range(len(M)):
            tempL = []
            for j in range(len(N[0])):
                temp = 0
                for c in range(len(M[0])):
                    temp = temp + M[i][c] * N[c][j]
                tempL.append(temp)
            tempM.append(tempL)
        return tempM
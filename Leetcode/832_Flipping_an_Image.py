class Solution:
    def flipAndInvertImage(self, A):
        i = 0
        j = len(A[0])-1

        while i < j:
            for row in range(len(A)):
                if A[row][i] != A[row][j]:
                    A[row][i], A[row][j] = A[row][j], A[row][i]
                A[row][i] ^= 1
                A[row][j] ^= 1
            i += 1
            j -= 1
        if i == j:
            for row in range(len(A)):
                A[row][i] ^= 1
        
        return A

    def flipAndInvertImageV2(self, A):
        # Official resolution implemented by Python2
        """
        In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
        helps us find the i-th value of the row, counting from the right.
        """
        for row in A:
            for i in range(int((len(row) + 1) / 2)):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

    
print(Solution().flipAndInvertImageV2([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
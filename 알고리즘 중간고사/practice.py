def division(matrix):  # 행렬 나누기
    n = len(A)
    m = n//2
    matrix_11=list([0] *m for i in range(m))  
    matrix_12=list([0] *m for i in range(m))
    matrix_21=list([0] *m for i in range(m))
    matrix_22=list([0] *m for i in range(m))
    for i in range(m):
        for j in range(m):
            matrix_11[i][j]=(matrix[i][j])
            matrix_12[i][j]=(matrix[i][j+m])
            matrix_21[i][j]=(matrix[i+m][j])
            matrix_22[i][j]=(matrix[i+m][j+m])
    return matrix_11, matrix_12, matrix_21, matrix_22

A_n ,A_m = map(int,input().split()) # A_n ,A_m은 각 A행렬의 행과 열
A = []
for i in range(A_n):
    A.append(list(map(int,input().split())))
print(A)
A_11,A_12,A_21,A_22 = division(A)

print(A_11, A_12, A_21, A_22)


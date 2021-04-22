def matrix_add(A,B):  # 행렬 덧셈
    n = len(A) # B해도 상관 없다
    C = []
    for _ in range(n):
        C.append([0]*n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C
def matrix_sub(A,B):  # 행렬 뺄셈
    n = len(A)  
    C = []
    for _ in range(n):
        C.append([0]*n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
def matrix_mul(A,B):  # 행렬 곱셈
    n = len(A)  
    C = [[0]*n for i in range(n)]
    for i in range(n):  
        for j in range(n):
            for k in range(n): 
                C[i][j] += A[i][k] * B[k][j]  
    return C
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


def solve(A,B): # 문제해결 함수 # A와 B의 크기가 같아야한다 n(행,열)은 2의 제곱이여야한다.
    global n
    m = len(A)
    if m == n//2:
        C = []
        C = matrix_mul(A,B)
        return C

    A11, A12, A21, A22 = division(A)
    B11, B12, B21, B22 = division(B)
    M1 = solve(matrix_add(A11,A22),matrix_add(B11,B22))
    M2 = solve(matrix_add(A21,A22),B11)
    M3 = solve(A11,matrix_sub(B12,B22))
    M4 = solve(A22,matrix_sub(B21,B11))
    M5 = solve(matrix_add(A11,A12),B22)
    M6 = solve(matrix_sub(A21,A11),matrix_add(B11,B12))
    M7 = solve(matrix_sub(A12,A22),matrix_add(B21,B22))
    C11 = matrix_add(matrix_sub(matrix_add(M1,M4),M5),M7)
    C12 = matrix_add(M3,M5)
    C21 = matrix_add(M2,M4)
    C22 = matrix_add(matrix_add(matrix_sub(M1,M2),M3),M6)
    
    for i in range(2):
        for j in range(2):
            print(C11[i][j],end=" ") # 각각에 for문이 돌아야함
        for j in range(2):
            print(C12[i][j],end=" ") # 각각에 for문이 돌아야함
        print()
    for i in range(2):
        for j in range(2):
           print(C21[i][j],end=" ")
        for j in range(2):
           print(C22[i][j],end=" ")
        print()





            
n = int(input())
# print("A행렬을 입력하세요")
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))

# print("B행렬을 입력하세요")
B = []
for _ in range(n):
    B.append(list(map(int,input().split())))

solve(A,B)
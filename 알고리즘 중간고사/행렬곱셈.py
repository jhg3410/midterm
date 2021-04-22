A_n ,A_m = map(int,input().split()) # A_n ,A_m은 각 A행렬의 행과 열
A = []
for i in range(A_n):
    A.append(list(map(int,input().split())))

B_n, B_m = map(int,input().split()) # B_n ,B_m은 각 B행렬의 행과 열
#  사실 행렬 곱셈에선 A의 행과 B의 열이 같아야해서 같은 변수로 해도 되지만 보기좋게 그냥 나누었다
B = []
for i in range(B_n):
    B.append(list(map(int,input().split())))

# C = [[0]*B_m for _ in range(A_n)]  # 행렬 A와 B를 곱한 행렬을 저장하기 위해 
C = [[0 for _ in range(B_m)] for _ in range(A_n)]   # 0으로 배열을 먼저 초기화 (각 출력또한 사진 첨부)

for n in range(A_n):  
    for k in range(B_m):
        for m in range(A_m):  # B_n으로 해도 상관없다 같기 때문에
            C[n][k] += A[n][m] * B[m][k]  # 그림으로 설명하기 

for c in C:
    print(c)

# for c in C:
#     for i in c:
#         print(i,end=" ")
#     print()    
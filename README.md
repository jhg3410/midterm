슈트라센 알고리즘이란 기존의 행렬곱셈 알고리즘에서 시간복잡도를 줄인 알고리즘이다.  
그래서 행렬곱셈을 먼저 구현하고 시간복잡도를 알아보고 다음에 슈트라센을 구현한 다음 알아보는 순서로 진행하겠습니다.  
먼저 구현한 행렬곱셈의 코드는 다음과 같고 설명은 주석으로 하겠습니다.
```{.python}
print("A행렬의 각 크기를 입력하세요")
A_n ,A_m = map(int,input().split()) # A_n ,A_m은 각 A행렬의 행과 열
A = []
for i in range(A_n):
    A.append(list(map(int,input().split())))
print("B행렬의 각 크기를 입력하세요")
B_n, B_m = map(int,input().split()) # B_n ,B_m은 각 B행렬의 행과 열
#  사실 행렬 곱셈에선 A의 행과 B의 열이 같아야해서 같은 변수로 해도 되지만 보기좋게 그냥 나누었다
B = []
for i in range(B_n):
    B.append(list(map(int,input().split())))

C = [[0]*B_m for _ in range(A_n)]  # 행렬 A와 B를 곱한 행렬을 저장하기 위해 0으로 배열을 먼저 초기화 

for n in range(A_n):  
    for k in range(B_m):
        for m in range(A_m):  # B_n으로 해도 상관없다 같기 때문에
            C[n][k] += A[n][m] * B[m][k] 
            
print("결과값:")
for c in C:
    for i in c:
        print(i,end=" ")
    print()    
```
출력값:  
![image](https://user-images.githubusercontent.com/80373033/115834943-b969f500-a450-11eb-908e-5ec3dd02bfeb.png)

위의 예제에서 처럼 4/4 행렬과 4/4행렬을 곱하면 8번의 곱셈과 4번의 뎃셈으로 구현된다.  
그러면 사실상 덧셈은 곱셈에 비해 걸리는 시간이 낮아 묻히고 곱셈으로만 n^3이 되어버린다  
그래서 기본적인 행렬곱셈의 시간복잡도는 n^3이다
```{.python}
def matrix_add(A,B):  # 행렬 덧셈
    n = len(A) # B해도 상관 없다
    C = []
    for _ in range(n):
        C.append([0]*n) # 결과를 넣을 배열 초기화
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C
def matrix_sub(A,B):  # 행렬 뺄셈
    n = len(A)  
    C = []
    for _ in range(n):
        C.append([0]*n) # 결과를 넣을 배열 초기화
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
def matrix_mul(A,B):  # 행렬 곱셈
    n = len(A)  
    C = [[0]*n for i in range(n)] # 결과를 넣을 배열 초기화
    for i in range(n):  
        for j in range(n):
            for k in range(n): 
                C[i][j] += A[i][k] * B[k][j] 
    return C
def division(matrix):  # 행렬 나누기
    n = len(A)
    m = n//2
    matrix_11=list([0] *m for i in range(m))  # 각 나눠질 배열 초기화
    matrix_12=list([0] *m for i in range(m))
    matrix_21=list([0] *m for i in range(m))
    matrix_22=list([0] *m for i in range(m))
    for i in range(m):
        for j in range(m):
            matrix_11[i][j]=(matrix[i][j])
            matrix_12[i][j]=(matrix[i][j+m]) # +m 을 넣어야 각 분할된 영역에 맞게 들어간다
            matrix_21[i][j]=(matrix[i+m][j])
            matrix_22[i][j]=(matrix[i+m][j+m])
    return matrix_11, matrix_12, matrix_21, matrix_22


def solve(A,B): # 문제해결 함수 # A와 B의 크기가 같아야한다 n(행,열)은 2의 제곱이여야한다.
    global n    # 기존 배열의 행(열)길이
    m = len(A)  # 새롭게 들어오는 행(열)길이
    if m == n//2: 
        C = []
        C = matrix_mul(A,B)   
        return C

    A11, A12, A21, A22 = division(A)  # 4분할로 나누기
    B11, B12, B21, B22 = division(B)
    M1 = solve(matrix_add(A11,A22),matrix_add(B11,B22))  # 나눈값들을 더한 다음 다시 solve함수 호출
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
    for i in range(n//2):
        # for j in range(n//2):        # 기본 반복문
        #     print(C11[i][j],end=" ")
        print(" ".join(str(C11[i][j])for j in range(n//2)),end= " ") # 한줄 반복문
        print(" ".join(str(C12[i][j])for j in range(n//2)),end= " ")
        print()
    for i in range(n//2):
        print(" ".join(str(C21[i][j])for j in range(n//2)),end= " ")
        print(" ".join(str(C22[i][j])for j in range(n//2)),end= " ")
        print()


n = int(input())  # 행(열) 길이 (같기 때문에 n으로 통일)
# print("A행렬을 입력하세요")
A = []  
for _ in range(n):
    A.append(list(map(int,input().split())))

# print("B행렬을 입력하세요")
B = []
for _ in range(n):
    B.append(list(map(int,input().split())))

solve(A,B)  # 함수 호출
```
시간복잡도:  
슈트라센에서도 4/4행렬과 4/4행렬을 곱하면 7번의 곱셈과 18번의 뎃셈이 필요하다  
뎃셈은 곱셈에 비해 걸리는 시간이 비교적 낮아 묻히고 그러면 7번의 곱셈만 계산하면  
n^2.807 정도가 소요되어서 기본 행렬곱셈보다 더 빠른 알고리즘이 된다.  
#출력문에서의 문제를 겪은 일:  
input()값:  
4  
1 2 3 4  
5 6 7 8  
9 1 2 3  
4 5 6 7  
8 9 1 2  
3 4 5 6  
7 8 9 1  
2 3 4 5  

나와야하는 값:  
[43, 53, 54, 37]  
[123, 149, 130, 93]  
[95, 110, 44, 41]  
[103, 125, 111, 79]  

처음 잘못 나온  값:
[[[43, 53], [123, 149]], [[54, 37], [130, 93]], [[95, 110], [103, 125]], [[44, 41], [111, 79]]]  
뭐가 잘못됬는지 몰랐다 m1에 print찍어보고 해도 잘 나왔는데 알고보니 넣을때 c11, c12순으로 넣다보니 분할되어 출력되어서 원래 우리가 알던 그 행렬로 안나왔던것이다

잘 못 나온값들을   
0 0  -> 1 0 -> 0 1 -> 1 1 -> 2 0 -> 3 0 -> 2 1 -> 3 1
이렇게 배열의 순서를 바꿔야 맞음 근데 바꾸기엔 알고리즘을 바꿔야해서 그러기보단 출력을 바꾸는게 더 좋다 생각
했지만 막상 출력하니 3중리스트라 내가 원하는 형태로 출력하려면 너무 코드가 더러워진다생각했다.  
![잘못된 출력(result_lst)](https://user-images.githubusercontent.com/80373033/115823176-ced72300-a440-11eb-8ec3-11aba920292f.png)  
그래서 result_lst를 쓰지않고 그냥 각각 분할된 C리스들을 바로 출력하면 더 깨끗하겠다 생각  

각 C리스트들을 출력하면 다음과 같다
![c11, c22, c33,c44 출력값](https://user-images.githubusercontent.com/80373033/115823087-abac7380-a440-11eb-9d66-aca5d056baf6.png)  

얘네들을 행렬방식으로  출력하기 위해선	
C11[0]-> C12[0] -> C11[1]->C12[1]->C21[0]->C22[0]->C21[1]->C22[1]
이렇게만 출력하면 리스트형태로 되어서 안의 index또한 표현할려면 2중리스트 모두 참조해야함
이 순서로 진행 되어야 함
한 줄 반복문을 이용해서 출력문 구현  
![image](https://user-images.githubusercontent.com/80373033/115835603-693f6280-a451-11eb-9a5c-567df5c83538.png)


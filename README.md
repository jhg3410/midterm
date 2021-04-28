### 슈트라센 알고리즘이란 기존의 행렬곱셈 알고리즘에서 시간복잡도를 줄인 알고리즘이다.  
그래서 행렬곱셈을 먼저 구현하고 시간복잡도를 알아본 다음 슈트라센 알고리즘을 알아보는 순서로 진행하겠습니다.  
구현한 행렬곱셈의 코드는 다음과 같고 설명은 주석과 슈트라센 알고리즘에서 하겠습니다.
```python
import time


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

start = time.time()

for n in range(A_n):  
    for k in range(B_m):
        for m in range(A_m):  # B_n으로 해도 상관없다 같기 때문에
            C[n][k] += A[n][m] * B[m][k]  # 그림으로 설명하기 
print("결과값:")
for c in C:
    for i in c:
        print(i,end=" ")
    print()   

print("기본 행렬 곱셈 알고리즘의 시간:",time.time()-start)
```
#### 출력값    
![image](https://user-images.githubusercontent.com/80373033/116014406-1b547580-a670-11eb-9ecc-6d94fe2b6395.png)   
8/8 행렬과 8/8 행렬을 곱했을때의 출력이다.  

### 시간 복잡도  
만약 이 알고리즘으로 4/4 행렬과 4/4행렬을 곱하면 8번의 곱셈과 4번의 뎃셈으로 구현된다.  
그러면 사실상 덧셈(n<sup>2</sup>)이 곱셈에 비해 걸리는 시간이 낮아 묻히고 곱셈으로만 n<sup>3</sup>이 되어버린다  
그래서 기본적인 행렬곱셈의 시간복잡도는 n<sup>3</sup>이다
* * *
### 슈트라센 알고리즘 구현
```python
import time

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
def division(matrix):  # 행렬 분할
    n = len(matrix)
    m = n//2
    matrix_11=list([0] *m for i in range(m))  # 각 분할될 배열 초기화
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

def conquer(matrix_11,matrix_12,matrix_21,matrix_22):  # 분할된 행렬 합치기
    n = len(matrix_11) 
    m = n*2  # 새로 만들어질 행렬의 길이
    new_matrix = list([0] *m for i in range(m))
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix_11[i][j]
            new_matrix[i][j+n] = matrix_12[i][j]
            new_matrix[i+n][j] = matrix_21[i][j]
            new_matrix[i+n][j+n] = matrix_22[i][j]
    return new_matrix


def solve(A,B): # 문제해결 함수 # A와 B의 크기가 같아야한다 n(행,열)은 2의 제곱이여야한다.    
    n = len(A)  # 새롭게 들어오는 행(열)길이

    if n == 2: # 행렬의 길이가 2일때 까지
        C = []
        C = matrix_mul(A,B)   
        return C

    A11, A12, A21, A22 = division(A)  # 4분할로 나누기
    B11, B12, B21, B22 = division(B)
    M1 = solve(matrix_add(A11,A22),matrix_add(B11,B22))  # 길이가 2가 될 때까지 재귀함수 호출
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
    
    C = conquer(C11,C12,C21,C22) # 분할된 행렬 합치기
    
    return C




n = int(input())  # 행(열) 길이 (같기 때문에 n으로 통일)
print("A행렬을 입력하세요")
A = []  
for _ in range(n):
    A.append(list(map(int,input().split())))
print("B행렬을 입력하세요")
B = []
for _ in range(n):
    B.append(list(map(int,input().split())))

start = time.time()
C = solve(A,B)  # 함수 호출

print("결과값:")

for c in C:
    for i in c:
        print(i,end=" ")
    print()

print("슈트라센 알고리즘 시간:",time.time()-start)
```  
### 코드 설명    
* 행렬 덧셈, 뺄셈  
![image](https://user-images.githubusercontent.com/80373033/116014654-3a073c00-a671-11eb-8281-6a03aa4d04db.png)  
위 사진은 행렬 덧셈과 뺄셈 함수를 구현한 것이다. 
매게 변수로 받아온 A또은 B의 길이를 가져온다 이는 행(열)의 길이이다.  
그리고는 결과값을 저장할 배열을 초기화한다. 
다음 단순히 A와 B배열의 각 요소들을 가져와 더해서 넣어주면 끝이다.  
뺼셈은 각 요소들을 빼서 넣어주면 된다.  
* 행렬 곱셈  
![image](https://user-images.githubusercontent.com/80373033/115869958-90aa2580-a479-11eb-9379-8b3101cb9146.png)  
위 사진은 행렬 곱셈이다. 한 줄 반복문을 사용해 결과값을 넣어줄 배열을 초기화한다.  
3중반복문을 사용해 처음보면 어려울 수 있지만 예시를 들어놓고 0,0부터 하나씩 순서대로 대입해보면
쉽게 구할 수 있다.  
* 행렬 분할  
![image](https://user-images.githubusercontent.com/80373033/115870498-4a08fb00-a47a-11eb-9373-8c4c8d7253d6.png)  
매개 변수로 받아온 행렬을 4분할 하는 함수코드이다.  
행렬의 길이를 가져온다. 그리고 2로 나눈값을 m에 저장하고 m의 크기만큼 2중 리스트를 만들어 초기화한다.  
그러고는 이제 기존 행렬의 값들을 분할된 행렬에 넣어주는데 주의해야할 점은 +m구문이다  
분할되다보니 각 영역에 맞게 들어가야한다. 그래서 m을 더해서 그 영역에 맞는 값들을 넣어준다.  
* 행렬 합치기  
![image](https://user-images.githubusercontent.com/80373033/115986218-25339580-a5ea-11eb-9660-349d0b538f5e.png)  
새로 만들어질 행렬은 패러미터로 받아오는 행렬들을 합치기에 길이가 2배여야해서 m을 만든다
새로운 리스트를 2중으로 m의 크기만큼 초기화하고 이제 새로운 리스트의 각 인자값에 
받아온 행렬들을 하나씩 각 자리에 맞게 넣어야한다. 그래서 n을 각각 더해줘야 자리에 맞게 들어간다.  
* 문제 해결 함수  
![image](https://user-images.githubusercontent.com/80373033/115994843-ab180680-a613-11eb-87ba-54835b2b8b1b.png)  
재귀함수를 사용한다. 
먼저 재귀함수를 끝내기 위한 조건문이 필요한데 행렬의 길이가 2이면 끝내는 걸로했다. 그래야 4/4 행렬들의 곱셈이면 7번의 곱셈이 호출되기때문이다.  
미리 정의해돈 division함수를 사용해 4분할로 나누어준다 그리고 이제 M1-M7로 재귀함수를 이용해서 계속해서 나눠주고 C11-C22까지 더한 다음 마지막 conquer함수로 합쳐주면서 올라온다.  
이것들이 재귀함수의 스택특성을 통해 결과값을 초래한다. 
* 입력과 출력(main)  
![image](https://user-images.githubusercontent.com/80373033/116014782-efd28a80-a671-11eb-8b7a-27e9d30cd8e7.png)  
행(열)의 크기를 입력받고 각 A,B 리스트를 초기화한 다음 입력받은 값들을 넣어주고 solve 함수를 호출해준다.  
그리고 return 값을 C로 받아주고 2중리스트이기에  for문을 이용해 각 리스트들의 요소들을 보기 좋게 출력해준다.  
또한 실행 시간을 보기 위해 함수 호출 전에 time.time으로 현재 시간을 넣어주고 끝난뒤엔 다시 time.time에서 start를 빼주면 실행 시간이 출력된다.  
* 출력값   
![image](https://user-images.githubusercontent.com/80373033/116014450-4d65d780-a670-11eb-9759-b93409d7ef23.png)  
8/8 행렬과 8/8 행렬간의 곱셈입니다. 보시면 위에서 했던 결과와 같은 걸 볼 수 있습니다.  

#### 시간복잡도    
슈트라센에서도 4/4행렬과 4/4행렬을 곱하면 7번의 곱셈과 18번의 뎃셈이 필요하다  
뎃셈은 곱셈에 비해 걸리는 시간이 비교적 낮아 묻히고 그러면 7번의 곱셈만 계산하면  
n<sup>2.807</sup> 정도가 소요되어서 기본 행렬곱셈보다 더 빠른 알고리즘이 된다.  
* * *
### 기본 행렬 곱셈 알고리즘과 슈트라센 알고리즘의 시간차이
16/16행렬과 16/16행렬을 곱했을때의 각 시간입니다  
* 기본 행렬 곱셈  
![image](https://user-images.githubusercontent.com/80373033/115995721-51b1d680-a617-11eb-93c8-7ce4b7ba1727.png)  

* 슈트라센  
![image](https://user-images.githubusercontent.com/80373033/115995835-ca189780-a617-11eb-942e-1544b256465a.png)  

보면은 우리가 유추한 결과와 다르다.   
왜냐면 기본 행렬곱셈에서의 행렬 덧셈보다 슈트라센에서의 행렬 덧셈이 더 많이 연산되기떄문이다.  
그럼에도 슈트라센이 더 시간복잡도가 낮은이유는 덧셈을 제외했기 때문이다.  
그럴려면 n이 엄청 커서 3제곱 한번이 많은 2제곱보다 커야하기때문이다.   

그래서 n을 엄청 크게 하고 실행해보았지만...  
![image](https://user-images.githubusercontent.com/80373033/116417048-e4e84780-a875-11eb-9ed1-9c8b49927eec.png)  
...  

* 그래프로 표현   
![image](https://user-images.githubusercontent.com/80373033/116402331-405f0900-a867-11eb-8fc7-44129f186f6c.png)  
빨간선이 기본 행렬 곱셈 알고리즘을 표현했고, 파란선이 슈트라센 알고리즘을 표현한 것이다.  
어느정도까진 빨간선이 성능이 높다가, n이 높아질수록 파란선이 어느순간 추월하게 된다.  

* * *  
### 구현 후 의문점을 느끼고 어려움을 겪은 일  
![image](https://user-images.githubusercontent.com/80373033/115874594-3a3fe580-a47f-11eb-80d6-b75acf8b19c5.png)  
처음엔 solve문을 이렇게 짰었다 그러고는 많은 예시를 넣어도 값이 제대로 나오는 것을 확인하고 끝냈다 생각해 markdown 작성 중이였다.  
그러던중 의문점이 생겼다. 이러면 8/8 행렬을 넣어도 if 문이 7번 나온다는 것이다. 
이렇게 되면 행렬 곱셈 함수가 호출되면서 작은 행렬의 행렬곱셈이 아닌 그저 길이를 2를 나눈 행렬이 곱셈 함수를 타게된다.  
이렇게 되어버리면 아무 의미가 없어진다. 이러면 시간복잡도가 곱셈연산이 1 줄어든 것 밖에 안된다.. 
재귀 함수의 이해가 아직 부족한 느낌이다. 수업시간에 배웠던 분할정복ppt를 보면서 다시금 구현해보려한다.  
분할 정복에 관해 다시 공부하니 알고보니 내가 구현한 코드에서는 합치는 함수를 구현을 안했던 것이다.  
위 사진처럼 짰었던 이유가 사실 분할은 하는데 합치는 함수를 구현 할 생각을 못 하고 분할을 하면 원래 길이의 반까지만  
분할을 해야 다시금 결과를 출력 할 때 원래의 n길이만큼 출력이 되니 n//2로 했었던 것이다.  
그래서 다시 conquer 함수를 구현하고 if문의 조건을 수정한 다음 재귀 함수를 호출하면 원래 목적의 시간복잡도를 가진 슈트라센 알고리즘이 나올거라 믿는다.  
그렇게 conquer을 짠 다음 각 c11,c12,c21,c22를 넣고 if문의 조건을 수정하니 원하던 알고리즘이 나오는게 확인되었다  

* * *
### 출력문에서의 문제를 겪은 일:  
(conquer 함수를 구현하지 않은 상태에서 겪었던 일이라 결과적으론 아무 의미가 없었습니다)  
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
![image](https://user-images.githubusercontent.com/80373033/115995912-2d0a2e80-a618-11eb-9884-42d54caa0774.png)  

결과적으로 conquer함수를 구현하고 합치다보니 위의 노력들이 의미가 없었다 그저 결과함수를 2중반복문으로 참조하면 원하는 형태로 나왔다.  
그래도 위의 노력도 하나의 공부이고 나중에 무조건 도움이 될거라 생각하고 놔둔다.  


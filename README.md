```{.python}
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
#     print()    8
```
4  
1 2 3 4  
5 6 7 8  
9 1 2 3  
4 5 6 7  
8 9 1 2  
3 4 5 6  
7 8 9 1  
2 3 4 5  

정답:
[43, 53, 54, 37]  
[123, 149, 130, 93]  
[95, 110, 44, 41]  
[103, 125, 111, 79]  

첨 잘못 나온  값:
[[[43, 53], [123, 149]], [[54, 37], [130, 93]], [[95, 110], [103, 125]], [[44, 41], [111, 79]]]
뭐가 잘못  되었는지 알고 표현
뭐가 잘못됬느지 몰랐다 m1에 print찍어보고 해도 잘 나왔는데 알고보니 넣을때 c11, c12순으로 넣다보니 분할되어 출력되어서 원래 우리가 알던 그 행렬로 안나왔던것이다


잘 못되게 나온 값
    0 0         0 1 	     1 0	      1 1	      2 0	       2 1	        3 0         3 1 		
[[[43, 53], [123, 149]], [[54, 37], [130, 93]], [[95, 110], [103, 125]], [[44, 41], [111, 79]]]

0 0  -> 1 0 -> 0 1 -> 1 1 -> 2 0 -> 3 0 -> 2 1 -> 3 1
이렇게 배열의 순서를 바꿔야 맞음 근데 바꾸기엔 알고리즘을 바꿔야해서 그러기보단 출력을 바꾸는게 더 좋다 생각
했지만 막상 출력하니 3중리스트라 내가 원하는 형태로 출력하려면 너무 코드가 더러워진다생각했다.
![잘못된 출력(result_lst)](https://user-images.githubusercontent.com/80373033/115823176-ced72300-a440-11eb-8ec3-11aba920292f.png)  
그래서 result_lst를 쓰지않고 그냥 각각 분할된 C리스들을 바로 출력하면 더 깨끗하겠다 생각

각 C리스트들을 출력하면 다음과 같다
![c11, c22, c33,c44 출력값](https://user-images.githubusercontent.com/80373033/115823087-abac7380-a440-11eb-9d66-aca5d056baf6.png)  

C11 - [[43, 53], [123, 149]]  
C12 - [[54, 37], [130, 93]]  
C21 - [[95, 110], [103, 125]]  
C22 - [[44, 41], [111, 79]]  
얘네들을 행렬방식으로  출력하기 위해선	
C11[0]-> C12[0] -> C11[1]->C12[1]->C21[0]->C22[0]->C21[1]->C22[1]
이렇게만 출력하면 리스트형태로 되어서 안의 index또한 표현할려면 2중리스트 모두 참조해야함
이 순서로 진행 되어야 함
한 줄 반복문을 이용해서 출력문 구현
![반복문출력](https://user-images.githubusercontent.com/80373033/115823187-d72f5e00-a440-11eb-8890-25dc793f041b.png)  
문제 발생 예제를 4*4했을 떄는 제대로 출력했었지만 8*8, 16*16을 input에 넣고 돌리면
4*4로 출력 발생
문제가 된 코드:

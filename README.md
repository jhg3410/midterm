# midterm
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
-------------사진--------
그래서 result_lst를 쓰지않고 그냥 각각 분할된 C리스들을 바로 출력하면 더 깨끗하겠다 생각

각 C리스트들을 출력하면 다음과 같다
-------------사진--------------
C11 - [[43, 53], [123, 149]]
C12 - [[54, 37], [130, 93]]
C21 - [[95, 110], [103, 125]]
C22 - [[44, 41], [111, 79]]
얘네들을 행렬방식으로  출력하기 위해선	

	
	

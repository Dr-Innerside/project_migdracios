# 6096 번 모범답안

# 빈 리스트 선언
from calendar import c
from cmath import e
from pyrsistent import b


d=[]
# 20X20 크기의 0이 담겨있는 리스트[리스트[0]] d생성
# 1,1을 만들기 위해서 비어있는 0번째를 포함하여 생성
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

# 바둑판 입력
for i in range(19) :
# 19자리의 바둑판의 바둑알 상태 입력
  a = input().split()
  for j in range(19):
    # 0,0으로 시작하는 바둑판을 
    # 1,1로 만들기 위해 인덱스에 1을 더하여 넣기
    d[i+1][j+1] = int(a[j])

# 카운트 입력
n = int(input())
for i in range(n) :
  # 위치를 바꿀 좌표 입력
  # x,y좌표를 입력해 x번째 행, y번째 열의 모든 바둑알을 뒤집는다
  x,y=input().split()
  x=int(x)
  y=int(y)
  # 사용하지 않을 0번째 를 제외한 19X19 리스트로 조회
  for j in range(1, 20) :
    # 바둑알이 0이라면 1로 바꾸기
    # y열 바꾸기
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    # x행 바꾸기
    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

# 바둑판 출력하기
for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()







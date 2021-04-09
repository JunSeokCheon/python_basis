# 파이썬은 구분자를 줄 바꿈인지 공백인지에 따라 다른 처리
# 줄 바꿈일 경우(입력)
n = int(input())
m = int(input())
print(n, m)

#공백일 경우(코딩 테스트에서 사용하는 전형적인 입력 소스 코드)
data = list(map(int, input().split())) # split : 공백으로 나누기, map : 모든 원소에 int 함수 적용
data.sort(reverse = True)
print(data)

# 입력의 개수가 많을 때(input 함수는 동작시간이 느림)
import sys

data = sys.stdin.readline().strip()
print(data)

# 출력시 문자열과 정수 충돌
answer = 7
print("정답은 " + str(answer) + "입니다.")

# 콤바로 구분하여 출력할 경우, 의도치 않은 공백이 삽입될수도 있다.
answer = 7
print("정답은", str(answer),"입니다.")

answer = 7
print(f"정답은 {answer}입니다.")
# sum, min, eval, sorted(default : 오름차순), factorial, sqrt, gcd, pi, e
result = sorted([9, 1, 5, 3, 6])
print(result)

# 리스트의 원소로 리스트나 튜플이 존재할때, 특정한 기준에 따라 정렬을 수행 가능. key 속성 이용
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1])
print(result)

# itertools 반복 처리 라이브러리
# permutations(리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 경우)
from itertools import permutations

data = ["A", "B", "C"]
result = list(permutations(data, 3))
print(result)

# combinations(permutations과 같지만 순서를 고려하지 않는 경우)
from itertools import combinations

data = ["A", "B", "C"]
result = list(combinations(data, 2))
print(result)

# product(permutations와 같지만 원소를 중복하여 뽑는 경우)
from itertools import product

data = ["A", "B", "C"]
result = list(product(data, repeat=2)) # repeat : product 객체를 초기화
print(result)

# combinations_with_replacement(combination과 같지만 원소를 중복해서 뽑는 경우)
from itertools import combinations_with_replacement

data = ["A", "B", "C"]
result = list(combinations_with_replacement(data, 2)) # repeat : product 객체를 초기화
print(result)

# 힙 기능을 위한 headq 라이브러리(최소힙) / PriorityQueue 보다 더 빠름
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 4, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 최대 힙 제공 x, 원소의 부호를 임시로 변경하는 방식
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 4, 7, 9, 2, 4, 6, 8, 0])
print(result)

# bisect("정렬된 배열"에서 특정한 원소를 찾아야 할 때)
# bisect_left(a,x) -> 정렬된 순서를 유지한 상태로 리스트 a에서 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a,x) -> 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a,x))  # 4를 리스트 a에 넣을 때 가장 왼쪽 인덱스는 2  (1 2 * 4 4 8)
print(bisect_right(a,x))  # 4를 리스트 a에 넣을 때 가장 오른쪽 인덱스는 4  (1 2 4 4 * 8)

# "정렬된 리스트"에서 "값이 특정 범위에 속하는 원소의 개수"를 구할 때
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))  # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3))  # 값이 [-1,3] 범위에 있는 데이터 개수 출력

# deque(스택과 큐의 기능 포함) <-> 기존 리스트는 append, pop으로 삽입/삭제할 경우 가장 뒤쪽 원소를 기준으로 수행 -> 가장 앞의 경우 많은 시간 소요
# deque - 첫 번째 원소를 제거할 때(popleft()), 마지막 원소를 제거할 때(pop())
# deque - 첫 번째 인덱스에 원소 x를 삽입할 때(appendleft(x)), 마지막 인덱스에 원소를 삽입할 때(append(x))
# deque의 큐 자료구조 경우는 삽입할 때 append, 삭제할 때 popleft()-> 선입선출
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data) # deque 형식으로 출력이 되기 때문에 리스트 자료형으로 변환
print(list(data))

# Counter(객체 내부의 원소가 몇 번씩 등장했는지 알려준다)
from collections import Counter

Counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(Counter['blue']) # 3
print(Counter['red'])  # 2
print(Counter['green']) # 1
"""
https://computer-science-student.tistory.com/313
https://codechacha.com/ko/python-2dimentional-array/
"""
"""
리스트 컴프리헨션 또는 배열*n 표현식을 이용한 배열 초기화방식
"""

"""
(1) 리스트 컴프리헨션을 이용한 배열 초기화
"""
n = 3
width = 5
arr = [[0]*width for i in range(5)]
print(arr, end="\n")

## 조금 더 직관적으로 하고 싶다면
arr = [[0]*3 for i in range(5)]
print(arr, end="\n")

## 또는 아래와 같이 초기화도 가능하다.
height = 5
width = 3
arr = [[0 for j in range(width)] for i in range(height)]
print(arr, end="\n")

rows = 5
cols = 3
arr = [[0 for j in range(cols)] for i in range(rows)]
print(arr, end="\n")

"""
(2) 배열*n 표현식을 이용한 배열 초기화
"""
## 더 직관적으로 초기화하면
arr = [[0]*3]*5
print(arr)

print(len(arr))
print(len(arr[0]))

# 그런데 이렇게 하면 의도하지 않은 값 까지 변경될 수 있다.
arr[0][0] = 5
print(arr)

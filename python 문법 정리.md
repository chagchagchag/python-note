## python 문법 정리

## time

https://www.daleseo.com/python-time/ 

- time 함수는 time 패키지 안에 있다. 따라서 from time 을 통해서 time 패키지에서 불러와야 한다. 
- sleep 함수는 time 패키지 안에 있다. 따라서 from time 을 통해서 time 패키지에서 불러와야 한다.

```python
from time import time, sleep

print("--- delayed [list]") # 3초 
def delayed_list_abc():
    list = []
    start = time()
    for c in list_abc():
        sleep(1)
        list.append(c)
    end = time()
    print(">>> ", (end-start))
    return list
delayed_list_abc()
```

<br/>



## generator : yield

https://www.daleseo.com/python-yield/

list

- list 를 사용하면 모든 결과 값을 메모리에 올려놓은 후 연산을 시작합니다..

yield

- yield 를 사용하면 결과값을 하나씩 메모리에 올려놓으면서 수행합니다. 
- yield 는 generator 라고 불리는 파이썬의 개념입니다. 



<br/>

그리고 yield 는 게으른 반복자 (lazy iterator) 라고도 불립니다. generator 의 lazy iterator 속성을 이용하면 효율적인 프로그램을 작성할 수 있습니다.<br/>

한번에 메모리에 모두 올리기에는 대용량의 데이터일 경우 스트림 방식의 데이터로 처리하게 되는데 이런 경우에 유용하게 사용할 수 있습니다.<br/>

generator 역시 list 처럼 comprehension 을 할 수 있습니다. 아래는 간단한 예제입니다.

```python
data = (c for c in "ABC")
for d in data:
    print(d)


```

<br/>



## generator comprehension

https://www.daleseo.com/python-yield/

list

- list comprehension 은 `[]` 을 사용합니다.

generator

- generator comprehension 은 `()` 을 사용합니다.

```python
print("--- generator comprehension ")
data = (c for c in "ABC")

for d in data:
    print(d)
```

<br/>

출력결과

```plain
A
B
C
```

<br/>



## heapq

https://www.daleseo.com/python-heapq/

Java 의 ProrityQueue 처럼 우선순위 큐 역할을 하는 파이썬의 우선순위 큐입니다. <br/>

min heap 으로 구성되어 있습니다.<br/>

heapq 모듈을 사용하면 파이썬의 일반 list 를 최소힙(min heap) 처럼 사용할 수 있습니다. (참고로 자바의 `PriorityQueue` 처럼 별도의 자료구조는 아닙니다.)<br/>

비어있는 리스트를 생성한 후에 heapq 모듈의 함수를 호출할 때 이 리스트를 넘겨서 heap 자료구조로 생성하는 방식으로 생성합니다.<br/>



사용법 1

```python
import heapq

heap = []
heapq.heappush(heap, (0, start))
value, destination = heapq.heappop(heap)
```

<br/>



사용법 2

```python
from heapq import heappush, heappop

heap = []
```

<br/>



### heap 자료구조 생성

```python
"""
heap 자료구조 생성
"""
def create_heap():
    heap = []
    heappush(heap, 5)
    heappush(heap, 1)
    heappush(heap, 3)
    heappush(heap, 7)

    print(heap)

print("===")
print("create_heap()")
create_heap()
```

<br/>

출력

```plain
===
create_heap()
[1, 5, 3, 7]
```

<br/>



### 힙에서 원소 제거

```python
"""
heap 에서 원소 제거
"""
def remove_element():
    heap = []
    heappush(heap, 5)
    heappush(heap, 7)
    heappush(heap, 3)
    heappush(heap, 1)

    print("removed ", heappop(heap))
    print(heap)

print("\n===")
print("remove_element()")
remove_element()
```

<br/>

출력

```plain
===
remove_element()
removed  1
[3, 7, 5]
```

<br/>



### 삭제 없이 원소 얻기 (peek())

```python
"""
삭제 없이 원소 얻기 (peek())
"""
def peek_element():
    heap = []
    heappush(heap, 5)
    heappush(heap, 7)
    heappush(heap, 3)
    heappush(heap, 1)

    print("current ", heap[0])
    print(heap)

print("\n===")
print("peek_element()")
peek_element()
```

<br/>

출력

```plain
===
peek_element()
current  1
[1, 3, 5, 7]
```

<br/>



### 기존 리스트를 힙으로 변환

```python
"""
기존 리스트를 힙으로 변환
"""
def list_heapify():
    list = [7, 3, 5, 1, 9]
    heapify(list)
    print(list)

print("\n===")
print("list_heapify()")
list_heapify()
```

<br/>



```python
===
list_heapify()
[1, 3, 5, 7, 9]
```

<br/>



### 최대힙

```python
"""
최대힙
"""
def max_heap():
    list = [9, 3, 1, 7, 5]
    heap = []

    for n in list:
        heappush(heap, (-n, n)) #  (-n, n) 은 (우선순위, 값) 입니다.
    
    while heap:
        print(heappop(heap)[1])

print("\n===")
print("max_heap()")
max_heap()
```

<br/>



```plain
===
max_heap()
9
7
5
3
1
```

<br/>



### n 번째 최소값/최대값

- 배열을 힙으로 만든 후 heappop() 을 n번 호출
- heapify() 함수로 힙으로 만든 후 heappop() 을 n 번 호출
- nsmallest(), nlargest() 사용

#### 배열을 힙으로 만든 후 heappop() 을 n번 호출

```python
"""
n 번째 최소, 최대
- 배열을 힙으로 만든 후 heappop() 을 n번 호출
"""
def find_nth_smallest_by_forloop(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)
    
    nth_min = None
    for num in range(n):
        nth_min = heappop(heap)
    
    return nth_min

print("\n===")
print("find_nth_smallest_by_forloop >>> ")
print(find_nth_smallest_by_forloop([1,5,3,7,9], 3))
print("\n")
```

<br/>



출력결과

```plain
===
find_nth_smallest_by_forloop >>>
5
```

<br/>



#### heapify() 함수로 힙으로 만든 후 heappop() 을 n 번 호출

```python
def find_nth_smallest_by_heapify(nums, n):
    heapify(nums)

    nth_min = None
    for i in range(n):
        nth_min = heappop(nums)
    
    return nth_min

print("\n===")
print("find_nth_smallest_by_heapify >>> ")
print(find_nth_smallest_by_heapify([1,5,3,7,9], 3))
print("\n")
```

<br/>



출력결과

```plain
===
find_nth_smallest_by_heapify >>>
5
```

<br/>



#### nsmallest(), nlargest() 사용

nsmallest(), nlargest()

```python
"""
n 번째 최소, 최대
- nsmallest(), nlargest() 사용
"""
from heapq import nsmallest
from heapq import nlargest

def find_nth_smallest_by_nsmallest():
    nth_min = nsmallest(3, [1,5,3,7,9])[-1]
    return nth_min
    
print("\n===")
print("find_nth_smallest_by_nsmallest >>> ")
print(find_nth_smallest_by_nsmallest())
print("\n")

def find_nth_largest_by_nlargest():
    nth_max = nlargest(3, [1,5,7,3,9])[-1]
    return nth_max

print("\n===")
print("find_nth_largest_by_nlargest >>> ")
print(find_nth_largest_by_nlargest())
print("\n")
```



### 힙 정렬

어떤 데이터를 insert 하면서 순서에 맞춘 자료로 읽어들일수 있으려면 heappush 를 통해 min-heap 에 데이터를 계속해서 insert 하면 됩니다.

```python
def get_sorted_heap(nums):
    heap = []
    for n in nums:
        heappush(heap, n)
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))

    return sorted_nums
print("\n===")
print("get_sorted_heap >>> ")
print(get_sorted_heap([1,5,3,7,9]))
print("\n")
```

<br/>



출력결과

```plain
===
get_sorted_heap >>>
[1, 3, 5, 7, 9]
```

<br/>



## 문자열 치환 - string.replace()

- https://yuddomack.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-replace-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A0%9C%EA%B1%B0-%EC%88%98%EC%A0%95%EB%B3%80%ED%99%98
- 

### replace(str1, str2)

```python
str = "1,2,3,4,5,6,7,8,9"

r1 = str.replace(",", "")
r2 = str.replace(",", "0")

print("r1 = ", r1)
print("r2 = ", r2)
```

<br/>



출력결과

```plain
r1 =  123456789
r2 =  10203040506070809
```

<br/>



### relace(str1, str2, from\_left)

```python
"""
좌측에서 cnt 개 만큼 변환
"""
str = "1,2,3,4,5,6,7,8,9"

r1 = str.replace(",", "", 3)
r2 = str.replace(",", "0", 3)

print("r1 = ", r1)
print("r2 = ", r2)
```

<br/>



출력결과

```plain
r1 =  1234,5,6,7,8,9
r2 =  1020304,5,6,7,8,9
```

<br/>



## 문자열 치환 - rsplit(s), join() : 오른쪽에서부터 치환 

```python
"""
우측에서 cnt 개 만큼 변환
"""
str = "1,2,3,4,5,6,7,8,9"

r1 = "".join(str.rsplit(",", 3))
r2 = "0".join(str.rsplit(",", 3))


print("r1 = ", r1)
print("r2 = ", r2)
```

<br/>

출력결과

```plain
r1 =  1,2,3,4,5,6789
r2 =  1,2,3,4,5,6070809
```

<br/>



## 문자열 치환 - string.split(), string.split(s)

```python
str1 = "hello world"
print(str1.split())
print("\n")

str2 = "hello:world"
print(str2.split(":"))
print("\n")
```

<br/>



출력결과

```plain
['hello', 'world']


['hello', 'world']
```

<br/>



## 슬라이싱

https://twpower.github.io/119-python-list-slicing-examples

슬라이싱(slicing), 슬라이스(slice) 는 연속적인 객체 자료형(e.g. 리스트, 튜플, 문자열)에 대해 범위를 지정하고 선택해서 원하는 객체를 가져오는 표기법/방법을 의미합니다.<br/>

슬라이싱을 하면 새로운 객체가 생성됩니다. 일부분을 복사해서 가져오게 됩니다.<br/>



### start, end, step

```python
arr[start:end:step]
```

- start : 슬라이싱을 시작할 위치를 의미합니다.
- end : 슬라이싱을 끝낼 위치입니다. end는 포함되지 않습니다.(=exclusive)
- step : 몇 step 씩 끊어서 가져올지, 방향(-/+)을 지정합니다. 

<br/>



### 인덱스를 읽는 방향 지정

- 양수 방향 : 연속적인 객체들의 제일 앞에서부터 차례로 읽는 방식입니다.
- 음수 방향 : 연속적인 객체들의 제일 뒤에서부터 차례로 읽는 방식입니다.

```plain
arr = ['a', 'b', 'c', 'd', 'e']
/ Index References
-------------------------------
|  a  |  b  |  c  |  d  |  e  |
-------------------------------
|  0  |  1  |  2  |  3  |  4  |          // 양수 방향
-------------------------------
| -5  | -4  | -3  | -2  | -1  |          // 음수 방향
-------------------------------
```

<br/>



### arr\[start : \]

```python
"""
arr[start:]
"""
arr = [1,2,3,4,5]

print(arr[1:])
print(arr[-3:])
```

<br/>

출력결과

```plain
[2, 3, 4, 5]
[3, 4, 5]
```

<br/>



### arr\[:end\]

```python
"""
arr[:end]
"""
arr = [1,2,3,4,5]

print(arr[:3])
print(arr[:-1])
```

<br/>

출력결과

```plain
[1, 2, 3]
[1, 2, 3, 4]
```

<br/>



### arr\[start:end\]

```python
"""
arr[start:end]
"""
arr = [1,2,3,4,5]

print(arr[2:4]) # [3,4]
print(arr[-4:-2]) # [2,3]
```

<br/>

출력결과

```plain
[3, 4]
[2, 3]
```

<br/>



### arr\[start​\:end:step\]

#### e.g.1

```python
"""
arr[start:end:step]
"""
arr = [1,2,3,4,5]

print(arr[3:0:-1])  # [4,3,2] 
                    # 참고: [4,3,2,1] 이 아니다. 
                    # end 는 exclusive 라는 점을 기억할 것.
```

<br/>

#### e.g.2

```python
# 처음부터 +2씩 하는데, 끝을 몰라서 지정을 안한 경우
arr = [1,2,3,4,5]
print(arr[::2]) # [1,3,5]
```

<br/>

#### e.g.3

```python
# -5 위치에서부터 +3 의 인덱스마다 한번씩 순회
arr = [1,2,3,4,5]
print(arr[-5::3]) # [1,4]
```

<br/>

#### e.g.4

```python
# 처음부터 뒷 방향으로 -1 씩 순회 
arr = [1,2,3,4,5]
print(arr[::-1]) # [5,4,3,2,1]
```

<br/>

#### e.g.5

```python
# index 2 에서부터 -1 만큼 이동
arr = [1,2,3,4,5]
print(arr[2::-1]) # [3,2,1]
```

<br/>



## iterator, itertools



## 클래스






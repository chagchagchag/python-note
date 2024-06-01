from time import time, sleep

print("---")
def list_abc():
    return list("ABC")

for c in list_abc():
    print(c)

print("--- ")
def yield_abc():
    yield "A"
    yield "B"
    yield "C"

for c in yield_abc():
    print(c)

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

print ("--- delayed [yield]") # 1초
def delayed_yield_abc():
    for c in "ABC":
        sleep(1)
        end = time()
        yield c
    
delayed_yield_abc()


## yield
"""
list 를 사용하면 모든 결과 값을 메모리에 올려놓은 후 연산을 시작한다.
yield 를 사용하면 결과값을 하나씩 메모리에 올려놓으면서 수행한다.

yield 는 generator 라고 불리는 파이썬의 개념입니다. 
그리고 yield 는 게으른 반복자 (lazy iterator) 라고도 불립니다. generator 의 lazy iterator 속성을 이용하면 효율적인 프로그램을 작성할 수 있습니다.

한번에 메모리에 모두 올리기에는 대용량의 데이터일 경우 스트림 방식의 데이터로 처리하게 되는데 이런 경우에 유용하게 사용할 수 있다.
"""


## yield from : list 에서부터 generator 생성
print("--- yield from generator")
def from_list_generator():
    yield from [1,2,3]

for i in from_list_generator():
    print(i)

print("--- generator comprehension ")
## generator comprehension
###  list comprehension 은 [] 을 사용한다.
###  generator comprehension 은 () 을 사용한다.
data = (c for c in "ABC")

for d in data:
    print(d)



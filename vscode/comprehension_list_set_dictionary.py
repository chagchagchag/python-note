"""
단순 컨셉을 알아보자
- list comprehnsion 의 반환값은 list 다!!
"""
list = [i*10 for i in range(1, 10)]
print(list, end = "\n")



"""
함수를 함께 사용하는 것 역시 가능하다.
"""
def append_day(num):
    return str(num) + " Day"

list = [append_day(i) for i in range(1, 10)]
print(list, end = "\n")


"""
조건문을 사용하는 것 역시 가능하다.
"""
print("홀수만 걸러내기", end = "\n")
list = [i for i in range(1, 10) if i%2 == 1]
print(list, end = "\n")

"""
조건문을 여러개 쓰는 경우도 있다.
"""
list = [i for i in range(1,10) if i%2 == 0 if i%3 == 0]
print(list, end = "\n")


"""
조건문을 왼쪽에 두는 경우 (1) : 단순 조건문
"""
list = [i%2 == 1 for i in range(1, 10)]
print(list, end = "\n")

"""
조건문을 왼쪽에 두는 경우 (2) : else 와 함께 사용하는 경우
= 이 경우 맨 왼쪽에 반환값을 두어야 한다.
"""
list = [i if i%2 == 1 else 'even' for i in range(1,10)]
print(list, end = "\n")


"""
중첩 컴프리헨션
"""
list = ["{0} x {1} = {2}".format(i, j, i*j) for i in range(1,2) for j in range(1, 10)]
print(list, end = "\n")
# ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '1 x 4 = 4', '1 x 5 = 5', '1 x 6 = 6', '1 x 7 = 7', '1 x 8 = 8', '1 x 9 = 9']

## 띄워서 쓰는 것 역시 가능하다
list = [
        "{0} x {1} = {2}".format(i, j, i*j) 
        for i in range(1,2) for j in range(1, 10)
]
print(list, end = "\n")
# ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '1 x 4 = 4', '1 x 5 = 5', '1 x 6 = 6', '1 x 7 = 7', '1 x 8 = 8', '1 x 9 = 9']


"""
Set 컴프리헨션
"""
odd_set = {i for i in range(1, 10) if i%2 == 1}
print(odd_set, end = "\n")
# {1, 3, 5, 7, 9}

"""
Dictionay 컴프리헨션
"""
dictionary_set = {i:i*10 for i in range(1,10)}
print(dictionary_set, end="\n")
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}



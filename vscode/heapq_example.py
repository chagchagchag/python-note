from heapq import heappush, heappop, heapify

"""
heapify
"""

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
print("\n")


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


"""
n 번째 최소, 최대
- heapify() 함수로 힙으로 만든 후 heappop() 을 n 번 호출
"""
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

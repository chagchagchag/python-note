"""
stack
"""

"""
- 파이썬에서는 stack 을 따로 제공하지 않는다. 
- 기본으로 제공되는 list 내에 stack 처럼 LIFO (Last In First Out) 방식으로 사용할 수 있는 메서드 들을 제공하고 있다.
"""

"""
stack 초기화
= stack = []
"""
stack = []
print(stack, end="\n")


"""
push
= stack.append(e)
"""
stack = []
for i in range(1,4):
    stack.append(i)
print(stack) # [1,2,3]


"""
pop
= stack.pop()
"""
stack = []
for i in range(1,4):
    stack.append(i)

last_element = stack.pop()
print(last_element) # 3
print("current stack = ", stack) # [1, 2]


"""
peek
= stack[-1]
"""
stack = []
for i in range(1,4):
    stack.append(i)

curr = stack[-1]
print(curr) # 3
print("current stack = ", stack) # [1, 2, 3]
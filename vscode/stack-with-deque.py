from collections import deque
stack = deque()

for i in range(1, 4):
    print(stack.append(i))

print("current stack = ", stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())


"""

"""
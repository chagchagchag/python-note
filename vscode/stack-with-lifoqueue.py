from queue import LifoQueue

## 헐 LifoQueue 라는 단어 자체가 모순이지 않나?
## 메서드도 병신같네. 그냥 deque 또는 list 쓰는게 나을 것 같다.

stack = LifoQueue(maxsize=3)
print(stack.qsize())


stack.put('a')
stack.put('b')
stack.put('c')


print('Full ? >> ', stack.full())
print("Size : ", stack.qsize())


print("\nElements popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty : ", stack.empty())

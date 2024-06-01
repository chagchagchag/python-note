"""
arr[start:]
"""
arr = [1,2,3,4,5]

print(arr[1:])
print(arr[-3:])


"""
arr[:end]
"""
arr = [1,2,3,4,5]

print(arr[:3])
print(arr[:-1])


"""
arr[start:end]
"""
arr = [1,2,3,4,5]

print(arr[2:4]) # [3,4]
print(arr[-4:-2]) # [2,3]


"""
arr[start:end:step]
"""
arr = [1,2,3,4,5]

print(arr[3:0:-1])  # [4,3,2] 
                    # 참고: [4,3,2,1] 이 아니다. 
                    # end 는 exclusive 라는 점을 기억할 것.


# 처음부터 +2씩 하는데, 끝을 몰라서 지정을 안한 경우
arr = [1,2,3,4,5]
print(arr[::2]) # [1,3,5]

# -5 위치에서부터 +3 의 인덱스마다 한번씩 순회
arr = [1,2,3,4,5]
print(arr[-5::3]) # [1,4]

# 처음부터 뒷 방향으로 -1 씩 순회 
arr = [1,2,3,4,5]
print(arr[::-1]) # [5,4,3,2,1]

# index 2 에서부터 -1 만큼 이동
arr = [1,2,3,4,5]
print(arr[2::-1]) # [3,2,1]
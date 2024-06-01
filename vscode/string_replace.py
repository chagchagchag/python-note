str = "1,2,3,4,5,6,7,8,9"

r1 = str.replace(",", "")
r2 = str.replace(",", "0")

print("r1 = ", r1)
print("r2 = ", r2)
print("\n")

"""
좌측에서 cnt 개 만큼 변환
"""
str = "1,2,3,4,5,6,7,8,9"

r1 = str.replace(",", "", 3)
r2 = str.replace(",", "0", 3)

print("r1 = ", r1)
print("r2 = ", r2)
print("\n")

"""
우측에서 cnt 개 만큼 변환
"""
str = "1,2,3,4,5,6,7,8,9"

r1 = "".join(str.rsplit(",", 3))
r2 = "0".join(str.rsplit(",", 3))


print("r1 = ", r1)
print("r2 = ", r2)
print("\n")



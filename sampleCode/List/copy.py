
li = [1, 2, 3, 4, 5, 6] # + [7,8,9]

mutableLi = li
immutableLi = li.copy()

li.extend([7, 8, 9])

print("li :", li, " id : ", id(li)) # [1, ... , 9]

print("mutableLi : ", mutableLi, " id : ", id(mutableLi)) # [1.. 9] 같다.
print("immutableLi : ", immutableLi, " id : ", id(immutableLi)) # [1.. 6] 다르다.

# 민자
# [1 .. 9, 7, 8, 9], 같다
# [1 .. 9], 다르다.

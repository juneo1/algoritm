#########################################################################################

# 입출력
# 
# 2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992


#########################################################################################
import sys

# 2557 Hello World
# print("Hello World!")

# 1000 A+B 
# a, b = map(int, input().split())
# print(a+b)

# 2558 A+B - 2
# a = int(input())
# b = int(input())
# print(a+b)

# 10950 A+B - 3
# count = int(input())

# for i in range(count):
#     a,b = map(int,input().split())
#     print(a+b)

# 10951 A+B - 4
# while True:
#     try:
#         a, b = map(int, input().split())
#     except:
#         break
#     print(a+b)

# 10952 A+B - 5
# while 1:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a+b)

# 10953 A+B - 6
# count = int(input())
# for i in range (count):
#     a, b = map(int, input().split(','))
#     print(a+b)

# 11021 A+B - 7
# count = int(input())

# for i in range(1, count+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a+b}")

# 11022 A+B - 8
# count = int(input())
# for i in range(1, count + 1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

# 11718 그대로 출력하기
while 1:
    try: 
        a = input()
    except:
        break
    print(a)


# 11719 그대로 출력하기 2
while 1:
    try: 
        a = input()
    except:
        break
    print(a)


# 11720 숫자의 합
count = int(input())
a = list(input())
sum = 0

for i in range(count):
    sum += int(a[i])

print(sum)


# 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992


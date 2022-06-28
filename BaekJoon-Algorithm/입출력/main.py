#########################################################################################

# 입출력
# 
# 2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992


#########################################################################################
import sys

# 2557 Hello World
print("Hello World!")


# 1000 A+B 
a, b = map(int, input().split())
print(a+b)


# 2558 A+B - 2
a = int(input())
b = int(input())
print(a+b)


# 10950 A+B - 3
count = int(input())

for i in range(count):
    a,b = map(int,input().split())
    print(a+b)


# 10951 A+B - 4
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)


# 10952 A+B - 5
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)


# 10953 A+B - 6
count = int(input())
for i in range (count):
    a, b = map(int, input().split(','))
    print(a+b)


# 11021 A+B - 7
count = int(input())

for i in range(1, count+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")


# 11022 A+B - 8
count = int(input())
for i in range(1, count + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")


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


# 11721 열 개씩 끊어 출력하기
a = input()
for i in range(0, len(a), 10):
    print(a[i:i+10])


# 2741 N 찍기
a = input()
for i in range(0, int(a)):
    print(i+1)



# 2742 기찍 N
a = input()
for i in range(int(a), 0, -1):
    print(i)



# 2739 구구단
a = int(input())
for i in range (1, 10):
    print(f"{a} * {i} = {a*i}")


# 1924 2007년
a, b = map(int, input().split())
day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range (1, a):
    day += month[i-1]

day += b
print(name[day%7])
    

# 8393 합
a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i

print(sum)

# 10818
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)


# 2438 별 찍기 - 1
cnt = int(input())

for i in range(1, cnt+1):
    print("*"*i)


# 2439 별 찍기 - 2
cnt = int(input())

for i in range(1, cnt+1):
    print(" "*(cnt-i) + "*"*i)
    

# 2440 별 찍기 - 3
cnt = int(input())

for i in range(cnt, 0, -1):
    print("*"*i)


# 2441 별 찍기 - 4
cnt = int(input())

for i in range(0, cnt+1):
    print(" "*(i) + "*"*(cnt-i))


# 2442 별 찍기 - 5
cnt = int(input())

for i in range(1, cnt+1):
    print(" "*(cnt-i) + "*"*(i) + "*"*(i-1))


# 2445 별 찍기 - 8
cnt = int(input())

for i in range(1, cnt+1):
    print("*"*(i) + " "*(cnt-i) + " "*(cnt-i) + "*"*(i))

for i in range(cnt-1, 0, -1):
    print("*"*(i) + " "*(cnt-i) + " "*(cnt-i) + "*"*(i))


# 2522 별 찍기 - 9
cnt = int(input())

for i in range(0, cnt):
    print(" " * (i) + "*" * (2 * (cnt - i) - 1))

for j in range(1, cnt):
    print(" " * (cnt - j - 1) + "*" * (2 * (j) + 1))



# 2446 



# 10991 별 찍기 - 16
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i) + "* " * (i-1) + "*")



# 10992 별 찍기 - 17
n = int(input())

for i in range(1, n+1):
    if (i==1 or i==n):
        print(" " * (n-i) + "*" * (2*i-1))
    else:
        print(" " * (n-i) + "*" + " "*(2*(i) - 3) + "*")


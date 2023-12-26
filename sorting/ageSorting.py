import sys

N = int(sys.stdin.readline().strip())
array = []
for i in range(N):
    age, name = map(str, input().split())
    array.append((int(age), name))

array.sort(key=lambda array:array[0]) #나이순대로만 정렬

for i in array:
    print(i[0], i[1])
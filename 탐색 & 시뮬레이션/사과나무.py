import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

start = end = n // 2
tot = 0
for i in range(n):
    for j in range(start, end + 1):
       tot += arr[i][j]
    if i < n // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
print(tot)
# https://codeforces.com/contest/2004/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n > 2:
        print("NO")

    else:
        if a[1] - a[0] > 1:
            print("YES")
        else:
            print("NO")
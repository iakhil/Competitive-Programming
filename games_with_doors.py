# https://codeforces.com/contest/2004/problem/B

t = int(input())

for _ in range(t):

    l, r = map(int, input().split())
    L, R = map(int, input().split())


    ans = 0
    
    il = max(l, L)
    ir = max(r, R)

    if ir >= il:
        ans += ir - il

    if min(l, L) < il:
        ans += 1

    if max(r, R) > ir:
        ans += 1
    
    print(ans)
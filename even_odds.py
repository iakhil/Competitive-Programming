# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())


if k - 1 >= n // 2:
    # present in even half
    if n % 2 == 0:
        l = k - (n//2)
        ans = 2 * l
    else:
        l =  (k- n//2) - 1
        ans = 2 * l
    
    if ans == 0:
        print(n)
    else:
        print(ans)
else:
    1, 3, 5, 7, 9, 2, 4, 6, 8
    ans = (2 * k) - 1
    print(ans)
    
    
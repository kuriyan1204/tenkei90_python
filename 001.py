n,l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))

def is_ok(m):
    #k+1個以上の長さm以上のピースに分類できるか？
    cnt = 0
    prev = 0
    for i in range(n):
        if (a[i] - prev)>=m and (l-a[i])>=m:
            cnt += 1
            prev = a[i]
    return cnt >= k


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(l+1,1-1))
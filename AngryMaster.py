def angryMaster(a,k):
    on_time = 0
    for i in a:
        if i <= 0 :
            on_time += 1;
    if on_time >= k:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    test_case = int(input())
    for i in range(test_case):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int,input().split()))
        print(angryMaster(a,k))
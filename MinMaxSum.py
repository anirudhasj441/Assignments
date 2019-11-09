def minMaxSum(li):
    min_sum = 0
    max_sum = 0
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]>li[j]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
    for i in range(1,len(li)):
        max_sum += li[i]

    for i in range(len(li)-1):
        min_sum += li[i]
    print(min_sum,end=" ")
    print(max_sum,end=" ")


if __name__ == "__main__":
    li = list(map(int,input().split()))
    minMaxSum(li)
    
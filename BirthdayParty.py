def sort(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i] < li[j]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
    return li
def birthdayParty(li):
    sort_li = sort(li)
    highest = 1
    for i in range(1,len(sort_li)):
        if sort_li[i] == sort_li[0]:
            highest += 1;
    return highest

if __name__ == "__main__":
    li = list(map(int,input().split()))
    print(birthdayParty(li))
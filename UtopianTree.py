def utopianTree(n):
    height = 0
    for i in range(n+1):
        if i == 0:
            height += 1
        elif i%2==0:
            height += 1
        else:
            height *= 2
    return height

if __name__ == "__main__":
    test_case = int(input())
    li = []
    for i in range(test_case):
        n = int(input())
        li.append(n)
    for i in  range(test_case):
        print(utopianTree(li[i]))



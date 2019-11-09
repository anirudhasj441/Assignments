import math
def rev(n):
    reverse = 0
    while n!=0:
        a = n%10
        reverse = (reverse*10)+a
        n = n//10

    return reverse
def beautifulDay(i,j,k):
    bd = 0
    for i in range(i,j+1):
        re = (i-rev(i))/k
        if re.is_integer():
            bd += 1
    return bd

if __name__ == "__main__":
    ijk  = list(map(int,input().split()))
    i = ijk[0]
    j = ijk[1]
    k = ijk[2]
    print(beautifulDay(i,j,k))
  
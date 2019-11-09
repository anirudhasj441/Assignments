def stairCase(n):
    for i in range(n):
        for j in range(n-1,i,-1):
            print(" ",end="")
        for k in range(i+1):
            print("#",end="")
        print()

if __name__ == "__main__":
    n = int(input("enter no of rows:"))
    stairCase(n)
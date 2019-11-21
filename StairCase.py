<<<<<<< HEAD
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
=======
def stairCase(n):
    st1=[]
    for i in range(n):
        st1.append(1)
    print(st1)

    for i in range(len(st1)):
        st1.append(st1[0]+st1[i])
    print(st1)



if __name__ == "__main__":
    # n = int(input('enter number of steps:'))
    n = 5
    stairCase(n)
>>>>>>> 30e85b513a6a8646a88d68bc5e130043d5a19eee

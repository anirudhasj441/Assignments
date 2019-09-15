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

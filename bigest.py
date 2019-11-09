def bigEliment(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]>li[j]:  
                b = li[i]
                break
    return b
    

if __name__ == "__main__":
    li = []
    print('enter eliments in list\nenter exit when finish!')
    while True:
        e = input(':')
        if e.isnumeric():
            e = int(e)
            li.append(e)
            
        else:
            break
    print(li)
    be = bigEliment(li)
    print(be)


li = []
rl = []
n = int(input('enter number of list items:'))
for i in range(n):
    e = input(':')
    li.append(e)

for i in range(len(li)-1,-1,-1):
    # print(i)
    rl.append(li[i])


print(li)
print(rl)
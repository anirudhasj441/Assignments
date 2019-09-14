def bigEliment(li):
	'''Returns the bigest eliment 
	from given list'''
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			if li[i]<li[j]:
				temp = li[i]
				li[i] = li[j]
				li[j] = temp
	return li[0]


if __name__ == "__main__":
	li = []
	print('enter eliments in list\nhit enter when complete!')
	while True:
		elm = input(':')
		if elm.isnumeric():
			elm = int(elm)
			li.append(elm)
		else:
			break
	#print(li)
	print(bigEliment(li))
	

def subString(s):
    c = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            s[i:j]
            c+=1
    return c
if __name__ == "__main__":
    s = input('Enter string:')

    print(subString(s))


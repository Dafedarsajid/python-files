s=input('Enter a number')
i=0
out=[]
temp=''
while i<len(s):
    if s[i]!=' ':
        temp+=s[i]
    else:
        out+=[temp]
        temp=''
    i+=1
else:
    if temp:
        out+=[temp]
print(out)            



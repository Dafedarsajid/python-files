a=input('Enter a string')
b=input('Enter a character')
i=0
count=0
while i<len(a):
    if a[i] in b:
        
        count+=1
i+=1
print(count)

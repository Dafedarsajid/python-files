a='rohit sharma'
out=''
res=''
for char in a:
    if char  not in out:
        out+=char
    else:
        res+=char
print(out)            
a=int(input( 'enter a 1st num'))
b=int(input('enter a 2nd num'))
c=input('enter a character')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print('a**b')
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
else:
    print("arithmatic operater")
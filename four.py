a=eval(input('enter a number'))
if type(a) in(int,float,complex,):
    print(a**2)
else:
    print(3*len(a)+1)
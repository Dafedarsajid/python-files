a=int(input("Enter a number: " ))
out=0
for i in range (1,a):
    if a%i==0:
        print(i,end='+')
        out+=i
if out==a:
    print("   is perfect number")
else:
    print(' is  not perfect number') 
       
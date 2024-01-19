a=float(input("enter percentage"))
if(a>90 and a<=100):
    print('A+')
elif(a<=90 and a>80):
    print('A')
elif(a<=80 and a>70):
    print('B+')
elif(70<=a>60):
    print("B")
elif(60<=a<=50):
    print("C")
elif(35<=a<=50):
    print("fail")
else:
    print("invalid percentage")
    




a= eval(input("enter a character"))
if a in '0123456789':
   print("digit")
elif a>='A' and a<='Z':
   print("upper case")
elif a>='a' and a<='z':
   print("lower case")
else:
   print("special char")
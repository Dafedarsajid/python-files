a=int(input("enter a ist num"))
b=int(input("enter a second num"))
c=int(input("enter a third num"))
if a>b and a>c:
    if b>c:
        print("b is a greatest number")
    else:
        print("c is a greatest num")
elif b>c:
     if a>c:
    print("a is the greatest num")
    else:
    print("c is the greatest number")
      else:
     if a>b:
    print("a is the greatest number")
else:
    print("b is a gretest number")

    
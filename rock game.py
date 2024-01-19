p1=input("now its your time P1")
p2=input("now it is a your time P2")
if p1==p2:
    print('tie')
elif p1=='scissor' and p2=='paper':
    print("p1 is winner")
elif p1=='rock' and p2=='scissor':
    print("p1 is a winner")
elif p1=='paper'and p2=='rock':
    print("p1 is a winner")
else:
  print("p2 win")

print("welcome to my bus")
dest=input('''
           select destination by entering
           1 for delhi
           2 for mumbai
           3 for chennai
           4 for hyderabad :''' )
adult_seats=int(input('number of Adults'))
child_seats=int(input('number of childrens'))
category=input('enter\n 1 for AC\n 2 for nonAC\n: ') 
distance={'1':2000,'2':800,'3':350,'4':500}
if category=='1':
    adult_price=5
    child_price=3
    total_price=(distance[dest]*(adult_price*adult_seats+child_price*child_seats))nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn                                                                                                            
    print("the total amount is :',total-prize,'rupees' ")
    confirm=input("enter 'yes' for confirm or press any other key to cancel :")
    if confirm=='yes':
        print("your transaction successfully ")
        print("thank you...\n visit again....\n Happy journey...")
    else:
        print('your transaction cancelled')
        print('thank you visit again')

          
          


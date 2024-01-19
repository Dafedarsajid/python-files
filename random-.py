import random
number=random.randint(10,100)
while True:
    a=int(input('enter a number'))
    if a==number:
        print('congrats! you guessed the number' ,a)
        break
    elif a<number:
        print('enter somne grater num')
    else:
        print('enter some lesser number')

         
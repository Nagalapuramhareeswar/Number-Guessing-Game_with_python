import random
random_number=random.randrange(0, 10)
print(random_number)
print("please ensure you have only three chances to guess the number")
for i in range(3):
    k=int(input("enter the number "+str(i)+" chance "+" : "))
    if(k>int(random_number)):
        print("greater number")
    elif(k<int(random_number)):
        print("lesser number")
    elif(k==int(random_number)):
        print("hoorahhhh....!!!!")
        break
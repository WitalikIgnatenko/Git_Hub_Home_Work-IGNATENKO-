import random
def myFunct(number):
    count = 0
    if number == 5:
        pass
    else:
        count += 1
        print(f'Number is', number)
        x = random.randint(0, 10)
        return myFunct(x)
myFunct(4)
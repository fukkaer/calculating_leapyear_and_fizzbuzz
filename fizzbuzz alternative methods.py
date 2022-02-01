#FizzBuzz alternative methods

for x in range(1,100):
    if x % 3 == 0:
        if x % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
        continue
    else:
        if x % 5 == 0:
            print('Buzz')
        else:
            print(x)

x = 1

while x != 100:
    if x % 3 == 0 or x % 5 == 0:
        if x % 5 == 0:
            if x % 3 == 0:
                print('FizzBuzz')
                x +=1
            else:
                print('Buzz')
                x +=1
        elif x % 3 == 0:
            if x % 5 == 0:
                pass
            else:
                print('Buzz')
                x+=1
    else:
        print(x)
        x +=1

y = 1

while y != 100:
    if y % 3 == 0 and y % 5 == 0:
        print('FizzBuzz')
        y+=1
    elif y % 3 == 0 or y % 5 == 0:
        if y % 3 == 0:
            print('Fizz')
            y+=1
        elif y% 5 == 0:
            print('Buzz')
            y+=1
    elif y % 3 != 0 and y % 5 != 0:
        print(y)
        y+=1

import time

#print(time.strftime('%X %x'))
#Used above print commamd to find out what format was used for time.

string_test = time.strftime('%X %x')
list_test = string_test.split(' ', 1)[1]

split_time = list_test.split('/', 2)[2]

test_num = float(split_time)

test_calc = test_num / 4

test_method = (test_calc).is_integer()

if test_method == True:
    print('is leapyear')
elif test_method == False:
    print('not leap year')


#Note: I've never heard of fizzbuzz before.

for x in range(1,100):
    if x % 15 == 0:
        print('Fizzbuzz')
        continue
    elif x % 3 == 0:
        print('Fizz')
        continue
    elif x % 5 == 0:
        print('Buzz')
        continue
    else:
        print(x)

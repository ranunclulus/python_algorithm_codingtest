def fibonacci(number):
    global zero_count, one_count
    if (number == 0):
        zero_count += 1
        return 0
    elif(number == 1):
        one_count += 1
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number -2)

zero_count, one_count = 0, 0
repeat_num = int(input())
for i in range(repeat_num):
    fibonacci_num = int(input())
    zero_count, one_count = 0, 0
    fibonacci(fibonacci_num)
    print(zero_count, one_count)
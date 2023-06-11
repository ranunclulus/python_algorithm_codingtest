fibonacci_num = []
for i in range(41):
    if (i == 0):
        fibonacci_num.append((1, 0))
    elif(i == 1):
        fibonacci_num.append((0, 1))
    else:
        fibonacci_num.append((fibonacci_num[i - 2][0] + fibonacci_num[i - 1][0],
                              fibonacci_num[i - 2][1] + fibonacci_num[i - 1][1]))

k = int(input())

for i in range(k):
    n = int(input())
    print(fibonacci_num[n][0], fibonacci_num[n][1])
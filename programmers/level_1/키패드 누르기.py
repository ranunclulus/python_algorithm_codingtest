def solution(numbers, hand):
    answer = ''
    keypad = [[10, 0, 10], 
              [7, 8, 9], 
              [4, 5, 6],
             [1, 2, 3]]
    right = [0, 2]
    left = [0, 0]
    col1 = [10, 7, 4, 1]
    col2 = [0, 8, 5, 2]
    col3 = [10, 9, 6, 3]
    for i in numbers:
        if i in col1:
            left[1] = 0
            left[0] = col1.index(i)
            answer += "L"
        if i in col3:
            right[1] = 2
            right[0] = col3.index(i)
            answer += "R"
        if i in col2:
            col = 1
            if(i == 0):
                row = 0
            elif(i == 8):
                row = 1
            elif(i == 5):
                row = 2
            else:
                row = 3
            rightlen = abs(right[0] - row) + abs(right[1] - col)
            leftlen = abs(left[0] - row) + abs(left[1] - col)
            if(rightlen < leftlen or (rightlen == leftlen and hand == "right")):
                answer += "R"
                right[0] = row
                right[1] = col
            else:
                answer += "L"
                left[0] = row
                left[1] = col
    return answer

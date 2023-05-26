def solution(left, right):
    answer = 0
    for elem in range(left, right+1):
        cnt = 0
        for i in range(1, elem + 1):
            if elem%i == 0:
                cnt += 1
        if cnt%2 == 0:
            answer += elem
        else:
            answer -= elem
    return answer

def solution(answers):
    submit = [[1, 2, 3, 4, 5],
             [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    cnt = [0, 0, 0]
    n1, n2, n3 = 0, 0, 0
    
    for elem in answers:
        if elem == submit[0][n1]:
            cnt[0] += 1
        if elem == submit[1][n2]:
            cnt[1] += 1
        if elem == submit[2][n3]:
            cnt[2] += 1
            
        n1 += 1
        n2 += 1
        n3 += 1
        
        if(n1 == 5):
            n1 = 0
        if(n2 == 8):
            n2 = 0
        if(n3 == 10):
            n3 = 0
    
    answer = []
    maxval = max(cnt)
    for i in range(len(cnt)):
        if (cnt[i] == maxval):
            answer.append(i + 1)
        
    return answer

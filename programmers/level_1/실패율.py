def solution(N, stages):
    clear = [0 for i in range(N+1)]
    stay = [0 for i in range(N+1)]
    fail = [0 for i in range(N+1)]
    answer = []
    
    for i in stages:
        if(i == 1):
            stay[0] += 1
        else:
            for j in range(i-1):
                clear[j] += 1
            stay[i-1] += 1
            
    for i in range(N):
        if(clear[i] + stay[i] == 0):
            fail[i] = 0
        else:
            fail[i] = stay[i] / (clear[i] + stay[i])

    for i in range(N):
        answer.append(fail.index(max(fail)) + 1)
        fail[fail.index(max(fail))] = -10
            
    return answer

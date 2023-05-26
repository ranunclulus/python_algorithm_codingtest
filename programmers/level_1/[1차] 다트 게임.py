def solution(dartResult):
    answer = []
    option = ['S', 'D', 'T', '*', '#']
    score = ''
    for i in range(len(dartResult)):
        if dartResult[i] not in option:
            score += dartResult[i]
        else:
            if (dartResult[i] == 'S'):
                answer.append(int(score))
                score = ''
            elif(dartResult[i] == 'D'):
                answer.append(int(score) * int(score))
                score = ''
            elif(dartResult[i] == 'T'):
                answer.append(int(score) * int(score) * int(score))
                score = ''
            elif(dartResult[i] == '*'):
                answer[len(answer) - 1] *= 2
                if(len(answer) >= 2):
                    answer[len(answer) - 2] *= 2
            elif(dartResult[i] == '#'):
                answer[-1] *= -1
            
        
    return sum(answer)

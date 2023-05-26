def solution(lottos, win_nums):
    answer = []
    same = 0
    lost = 0
    label = [0, 0, 0, 0, 0, 0]
    
    for i in range(6):
        for j in range(6):
            if(label[j] != 1 and lottos[i] == win_nums[j]):
                label[j] = 1
                same += 1
        if(lottos[i] == 0):
            lost += 1
    
    if(same+lost == 6):
        answer.append(1)
    elif(same+lost == 5):
        answer.append(2)
    elif(same+lost == 4):
        answer.append(3)
    elif(same+lost == 3):
        answer.append(4)
    elif(same+lost == 2):
        answer.append(5)
    else:
        answer.append(6)
    
    if(same == 6):
        answer.append(1)
    elif(same == 5):
        answer.append(2)
    elif(same == 4):
        answer.append(3)
    elif(same == 3):
        answer.append(4)
    elif(same == 2):
        answer.append(5)
    else:
        answer.append(6)
        
    return answer
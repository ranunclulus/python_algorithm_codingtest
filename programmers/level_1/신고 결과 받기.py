def solution(id_list, report, k):
    answer = []
    
    number = {}
    for i in id_list:
        number[i] = []
        answer.append(0)
        
    for i in range(len(report)):
        space = report[i].find(" ")
        from_id = report[i][:space]
        to_id = report[i][space + 1:]
        if from_id not in number[to_id]:
            number[to_id].append(from_id)
        
    for i in id_list:
        if(len(number[i]) >= k):
            for j in number[i]:
                index = id_list.index(j)
                answer[index] += 1
        
    return answer

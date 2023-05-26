def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    available = ['-', '_', '.']
    for i in range(len(new_id)):
        if(new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in available):
            answer += new_id[i]
            
    # 3단계      
    while (answer.find("..") != -1):
        answer = answer.replace("..", ".")
        
    # 4단계
    id_list = list(answer)
    if(id_list[0] == "."):
        del(id_list[0])
    if(len(id_list) != 0):
        if(id_list[-1] == "."):
            del(id_list[-1])
            
    # 5단계
    if(len(id_list) == 0):
        id_list.append('a')
        
    # 6단계
    if(len(id_list) > 15):
        del(id_list[15:])
    if(len(id_list) != 0):
        if(id_list[-1] == "."):
            del(id_list[-1])
            
    # 7단계
    if(len(id_list) < 3):
        while(len(id_list) < 3):
            id_list.append(id_list[-1])
        
    answer = ''
    for i in id_list:
        answer += i
    return answer

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for elem in arr1:
        elem = bin(elem)
        map1.append(str(elem)[2:].zfill(n))
        
    for elem in arr2:
        elem = bin(elem)
        map2.append(str(elem)[2:].zfill(n))
    
    for i in range(n):
        line = ""
        for j in range(n):
            if(map1[i][j] == "1" or map2[i][j] == "1"):
                line += "#"
            else:
                line += " "
        answer.append(line)
        
    return answer

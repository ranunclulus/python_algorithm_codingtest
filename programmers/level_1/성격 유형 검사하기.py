def solution(survey, choices):
    answer = ''
    #알파벳마다 값을 저장하는 Dictionary 설정
    category = {"R":0,
               "T":0,
               "C":0,
               "F":0,
               "J":0,
               "M":0,
               "A":0,
               "N":0}
    for i, choice in enumerate(choices):
        #점수가 4보다 작다면 문자열의 앞에 위치한 key를 갖는 item에 절댓값 4-점수 추가
        if choice <= 4:
            category[survey[i][0]] += abs(4-choice)
        #점수가 4보다 크다면 문자열의 뒤에 위치한 key를 갖는 item에 절댓값 4-점수 추가
        else:
            category[survey[i][1]] += abs(4-choice)
    #Dictionary는 index 접근이 불가능해서 list로 바꿔 주기
    values = []
    for key, value in category.items():
        value = [key, value]
        values.append(value)
    #바꾼 list를 2칸씩 iteration
    for i in range(0, 7, 2):
        #첫 알파벳의 점수가 더 크다면 첫 알파벳
        if values[i][1] > values[i+1][1]:
            answer += values[i][0]
        #두 번쨰 알파벳의 점수가 더 크다면 두 번쨰 알파벳
        elif values[i][1] < values[i+1][1]:
            answer += values[i+1][0]
        #두 알파벳의 점수가 동일하다면 사전적으로 먼저 있는 알파벳
        elif values[i][0] < values[i+1][0]:
            answer += values[i][0]
        else:
            answer += values[i+1][0]
    return answer
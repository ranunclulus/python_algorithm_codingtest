def solution(today, terms, privacies):
    answer = []
    # today를 특수 문자 제거하고 int형으로 캐스팅
    today = int(today.replace(".", ""))

    for i in range(len(privacies)):
        #privacies의 아이템이 특수 문자 제거된 채 [2023, 03, 13, A] 형식으로 저장
        privacy = privacies[i]
        privacy = privacy.replace(".", " ").split()

        for term in terms:
            #terms의 아이템이 [A, 3] 형태로 저장
            term = term.split()
            #만약 약관 종류가 같다면
            if privacy[3] == term[0]:
                #달에다가 추가하기
                privacy[1] = int(privacy[1]) + int(term[1])
        #업데이트한 달이 12보다 크면 년을 올리고 달은 다시 1~12 범위로 설정
        if privacy[1] > 12:
            privacy[0] = str(int(privacy[0]) + (privacy[1] // 12))
            privacy[1] = (privacy[1] % 12)
            #월이 10보다 작으면 0 추가 3 -> 03
        if privacy[1] < 10:
            privacy[1] = "0" + str(privacy[1])
        else:
            privacy[1] = str(privacy[1])
        #privacy 첫 항목에 str으로 날짜 저장
        privacy[0] = privacy[0] + str(privacy[1]) + privacy[2]
        #만약 오늘보다 늦었다면
        if int(privacy[0]) <= today:
            #답안에 index+1
            answer.append(i+1)
    return answer

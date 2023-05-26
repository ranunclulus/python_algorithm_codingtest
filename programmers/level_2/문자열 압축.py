def solution(s):
		#입력된 문자열의 크기가 1일 경우 비교군이 없음
    if len(s) == 1:
        return 1
    answers = []
    answer = ""
    for i in range(1, len(s)):
        #문자열을 i 크기로 자름
        note = [s[j:j+i] for j in range(0, len(s), i)]
        #같은 문자열 등장하면 카운트
        count = 1
        #문자열 순회하면서 answer 만들기
        for j in range(len(note) - 1):
            if note[j] == note[j+1]:
                count += 1
            else:
                if count == 1:
                    answer += str(note[j])
                else:
                    answer += (str(count) + str(note[j]))
                count = 1
        if count == 1:
            answer += str(note[-1])
        else:
            answer += (str(count) + str(note[-1]))
        answers.append(len(answer))
        answer = ""
    print(answers)
    return(min(answers))
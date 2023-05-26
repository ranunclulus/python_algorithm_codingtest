def solution(record):
    answer = []
    result = {}
    
    for event in record:
        info = list(event.split())
        if info[0] == "Enter" or info[0] == "Change":
            result[info[1]] = info[2]
    for event in record:
        info = list(event.split())
        if info[0] == "Enter":
            answer.append(f"{result[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(f"{result[info[1]]}님이 나갔습니다.")
    return answer

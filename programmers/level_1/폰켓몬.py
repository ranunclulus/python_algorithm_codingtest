def solution(nums):
    n = len(nums)/2
    character = list(set(nums))
    if(len(character) > n):
        return n
    else:
        return len(character)

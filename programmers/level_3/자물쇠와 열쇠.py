def turn(key, m):
    result = []
    for i in range(m):
        temp = []
        for j in range(m):
            temp.append(key[j][i])
        result.append(temp[::-1])
    return result

def check(new_lock, n):
    for i in range(n):
        for j in range(n):
            if new_lock[i+n][j+n] != 1:
                return False
    return True

def solution(key, lock):
    n, m = len(lock), len(key)
    #3배 큰 자물쇠 만들고 중앙을 채우기
    new_lock = [[1] * (3*n) for i in range(3 * n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    #4번 회전하는 동안
    for spin in range(4):
        for i in range(2*n):
            for j in range(2*n):
                #열쇠 꽂기
                for key_x in range(m):
                    for key_y in range(m):
                        new_lock[i+key_x][j+key_y] += key[key_x][key_y]
                if check(new_lock, n):
                    return True
                else: #열쇠 빼기
                    for key_x in range(m):
                        for key_y in range(m):
                            new_lock[i+key_x][j+key_y] -= key[key_x][key_y]
        key = turn(key, m)
    return False
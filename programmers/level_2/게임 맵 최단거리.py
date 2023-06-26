from collections import deque

def solution(maps):

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 벽을 벗어날 경우
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽으로 막혀 있는 경우
                if maps[nx][ny] == 0:
                    continue
                # 처음 지나가는 길이면 거리로 값을 바꿔 놓음
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        # 맨 마지막 칸 반환하기
        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer

maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

print(solution(maps))
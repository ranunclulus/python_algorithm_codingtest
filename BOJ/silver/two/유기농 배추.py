from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m, farm, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    result = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= m and 0 < ny <= n and farm[nx][ny] and visited[nx][ny] == 0:
                result.append((nx, ny))
                x, y = nx, ny
    return result


n, m, k = map(int, input().split())
farm = [[0 for i in range(m)] for j in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
for j in range(k):
    x, y = map(int, input().split())
    farm[x][y] = 1

count = 0
for i in range(n):
    for j in range(m):
        result = bfs(i, j, n, m, farm, visited)
        if (len(result) != 0):
            count += 1

print(count)

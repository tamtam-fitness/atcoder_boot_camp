from collections import deque


def bfs():
    #新しく探索用のものを作成
    d = [[float("inf")] * c for i in range(r)]
    #    右, 上, 左, 下
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    #スタートをいれる
    que.append((sy, sx))
    #探索するたびに、進んだ際の値を代入する。
    d[sy][sx] = 0
    
    while que:
        p = que.popleft()
        #popしたものがゴールか判断
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            #四方向にすすむ
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            #指定いる座標が迷路内か判定
            if 0 <= nx < r and 0 <= ny < c :
                #指定した座標が塀ではないか判定
                if maze[nx][ny] != "#" :
                    #指定した座標が未開拓であることを判定
                    if d[nx][ny] == float("inf"):
                        que.append((nx, ny))
                        #新しく開拓する場所に、既に開拓した場所の値を+1し代入させる
                        d[nx][ny] = d[p[0]][p[1]] + 1
    #popした際の進んだ値を返す
    return d[gy][gx]

# 縦　＊　横
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sx -= 1
sy -= 1
gy -= 1
gx -= 1

maze = [list(input()) for i in range(r)]

print(bfs())
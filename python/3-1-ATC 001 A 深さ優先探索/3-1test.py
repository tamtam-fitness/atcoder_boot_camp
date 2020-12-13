# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので、それを変更
import sys
sys.setrecursionlimit(10**7)


def dfs(x, y):
    #到達地点を 1として塗りつぶす
    d[x][y] = 1

    # 移動4方向をループ
    for i in range(4):
        #nx = 現時点のx座標plus + 上下左右
        nx = x + dx[i]
        #ny = 現時点のy座標plus + 上下左右
        ny = y + dy[i]

        # nx と ny が街の範囲内かどうかを判定
        if 0 <= nx and nx < n and 0 <= ny and ny < m :
            #nx と ny での座標がまだ未到達かを判定
            if d[nx][ny] == 0 :
                #nx と ny での座標が塀ではないかを判定
                if c[nx][ny] != "#": 
                    dfs(nx, ny)

#与えられた値をそれぞれintとして保存
n, m = map(int, input().split())

#高橋君が住む街長方形の形している町の状態を取得(格子状の区画)
c = [list(input()) for i in range(n)]

# 到達したかどうか（0は未到達、1は到達済み）
d = [[0] * m for i in range(n)]

# 移動する4方向: 右(1,0) , 上(0,1), 左(-1,0), 下(0,-1)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# スタート地点から dfs を始める
for i in range(n):
    for j in range(m):
        #x, y座標でsがあるかどうかを判定
        if c[i][j] == "s":
            #探索をスタート
            dfs(i, j)

# ゴール地点に到達したかどうか
for i in range(n):
    for j in range(m):
        #ゴールの地点が 1(塗り潰されている)かどうかを判定
        if c[i][j] == "g" and d[i][j]:
            print("Yes")
            exit()
print("No")
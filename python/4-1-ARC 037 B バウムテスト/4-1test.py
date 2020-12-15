#連結成分を　まず　割り出し、そこから　閉路があったらリターンさせる的な？？

#Nが頂点の数 Mが辺の数
N, M = [ map(int, input().split())]

#ここで頂点にから配列を設定。
g = [[] * N for i in range(N)]


for i in range(M):
    #辺からなるものを取得
    u, v = map(int, input().split())
    #配列は0行目からであるためデクリメントする
    u -= 1
    v -= 1
    
    #頂点と頂点がつながっている数字をそれぞれ格納
    g[u].append(v)
    g[v].append(u)


# 訪れたことがあるか
memo = [False for i in range(n)]


ans = 0
# 頂点をループ
for i in range(n):
    #訪れていない場合
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            # 閉路がなければ木である
            ans += 1
print(ans)
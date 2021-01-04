sd = input()
t = input()

n = len(sd)
m = len(t)

# sd を後ろから見ていき、 t の入りそうな場所を探す
                # n-m     0
for i in range(n - m, -1, -1):
    t_kamo = sd[i:i + m]
    for j in range(m + 1):
        # 1文字ずつ順に入りうるか調べ、最後まで入るなら "?" を "a" に置き換えて出力
        if j == m:
            print((sd[:i] + t + sd[i + len(t):]).replace("?", "a"))
            exit()
        #全部ハテナになっているかを確認
        if t_kamo[j] == "?":
            continue
        elif t_kamo[j] != t[j]:
            break

print("UNRESTORABLE")
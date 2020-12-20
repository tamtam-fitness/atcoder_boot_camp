n_m_t = list(map(int, input().split(" ")))

N = n_m_t[0]
max_N = n_m_t[0]

M = n_m_t[1]
T = n_m_t[2]

a_b_list = [ list(map(int, input().split(" "))) for _ in range(M)]

tmp = 0

for a_b in a_b_list:
    a = a_b[0]
    b = a_b[1]

    low_amount = a - tmp 
    #下げる
    N -= low_amount
    if N <= 0:
        print("No")
        exit()
    
    up_amount = b - a
    N += up_amount

    if max_N <= N:
        N = max_N

    tmp = b

#残りのtimeでバッテリーを削る
low_amount = T - tmp
N -= low_amount

if 0 < N:
    print("Yes")
else:
    print("No")

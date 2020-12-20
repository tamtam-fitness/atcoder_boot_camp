# バッテリー容量は N
#時刻 0時からスタート
# 途中で M回カフェを訪れ、時刻 Tに帰宅
#   N  M  T
# 10 2 20  
# 9 11
# 13 17

# step1 : 9時になるまで  n = floor(9 - 0.5)　へる ->　今回だと8

# step1 : 9 ~ 11で　2増える

# step1 : 9時になるまで  n = floor(9 - 0.5)　へる ->　今回だと8


n_m_t = list(map(int, input().split(" ")))

N = n_m_t[0]
M = n_m_t[1]
T = n_m_t[2]

a_b_list = [ list(map(int, input().split(" "))) for _ in range(M)]


# n + 0.5 -> で 時間軸作っておいて、if　で回復させるか減らすかの指定はどう？？

#whileで帰宅になるまでバッテリーの増減をトレースする

battery_action_time = 0.5 

while battery_action_time <= T:
    
    is_between_a_b = False
    for a_b in a_b_list:
        #カフェ開始　　　                                             カフェ終了
        if a_b[0] <= battery_action_time and battery_action_time  <= a_b[1]:
            N += 1 
            is_between_a_b = True
            break

    if not is_between_a_b:
        N -= 1

    if N <= 0:
        print("No")
        exit()
    
    battery_action_time += 1

print("Yes")


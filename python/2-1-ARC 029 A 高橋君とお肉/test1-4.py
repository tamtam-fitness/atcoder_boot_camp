from typing import List
  
def solve_takahashi_and_meat(meat_time_list: List[int]) -> int :

  # ==============================================================
  # return: 焼き時間の違う複数のお肉のリストが入力されると、２枚のグリルで焼く最小時間を返す
  # pre: [4, 6, 7, 10] 
  # post:　14 → aのグリルに[4, 10] bのグリルに[6, 7] で焼く。
  # ==============================================================

  # ★ step1 お肉の焼き時間の配列を降順に並び替える
  # ★ step2 焼き時間が大きい順からfor文で回し、２枚のグリルで焼き時間が小さい方にお肉を追加させる
  # ★ step3 最終的にa, bで焼き時間が大きい方を返す


  # 10, 7, 6,1 と降順で配列に格納する
  sorted_meat_time_li = sorted(meat_time_list, reverse = 1)

  #2枚のグリル初期値の設定をする
  gril_a = [0]
  gril_b = [0]
　
  #焼き時間が大きい順から回す
  for meat_time in sorted_meat_time_li:
    #現時点での総焼き時間を比較し小さい方にお肉を追加
    if sum(gril_a) >= sum(gril_b) :
      gril_b.append(meat_time)
    else :
      gril_a.append(meat_time)
  #aとbで総焼き時間が大きい方を返す
  return max(sum(gril_a), sum(gril_b))


N = int(input())
meat_time_list = [int(input()) for _ in range(N) ]
print(solve_takahashi_and_meat(meat_time_list))


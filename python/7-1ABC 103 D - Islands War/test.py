from operator import itemgetter

# ==============================================================
  # return: N個の島とM個の島と島を行き来させない要望が与えられた時、最低何個の橋を取り除けば良いのか出力
  # pre:  5 2   
        # 1 4
        # 2 5
  # post:　1 -> 2と4の間の橋のみを取り除けば1,4 2,5の行き来ができなくなる。ex) 1 2  x  4  5
  # ==============================================================

  # ★ step1  問題文をN,Mをint型にして変数にする
  # ★ step2  与えられたa,bの要望をbが小さい順にソートする
  #                      -> 実装:与えられた要望a bの間の橋を取り除き、行き来ができないようにする。
  #                         idx a b
  #                      -> 0:  1 3                    1 2
  #                         1:  2 4　なら2,3の間を除外    2 3  なら 1,2 2,3の間を除外
  #                      ->前bのより次のaが小さければ橋を1つ除外, 前bのより次のaが大きければ橋が２つ除外
  #                      ->bを小さい順にソートして、前のbの値を次のaの値でみて橋を取り除くかどうかみれるようにする
  # ★ step3 次のaの値が前のbの値以上であるかどうか判定
  # ★ step4 次のaの値が前のbの値以上であれば取り除く個数をインクリメントさせ前のbの値を現在のbの値で更新させる


#NとMを取得
N, M = map(int, input().split())

#M個の島のindexのa,bの行き来させない要望 を配列として取得
ab_requests =  [tuple(map(int, input().split())) for _ in range(M)]

#bの値が小さい順にソートする
#documentをみると key=itemgetter(num)が良さそう https://docs.python.org/3/howto/sorting.html
ab_requests_sorted = sorted(ab_requests,key=itemgetter(1))


pre_b = -1
next_a = -1
removed_counts = 0

for a, b in ab_requests_sorted :
  #次のaとして利用する
  next_a = a
  #次のaの値が前のbの値以上であるかどうか判定
  # より大きいケース[(1,2),(3,4)] と 以上のケース[(1,2),(2,3)]に注意
  if pre_b <= next_a :
    #取り除く橋の個数をインクリメントさせる
    removed_counts += 1
    #前のbを更新させ、次のaと値を比べられるようにする
    pre_b = b 

#結果を出力
print(removed_counts)


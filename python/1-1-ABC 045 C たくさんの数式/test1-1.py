

def solve_many_formulas(num: int) -> int :
    # ==============================================================
    # return: ある整数値を代入すると、数と数の間に+を入れてできる数式の和の合計を返す
    # pre: 125
    # post:　176 = (125) + (26 = 1+25) + (17 = 12+5) + (8 = 1+2+5) 
    # ==============================================================

    # ★ step1 整数値を文字列にし、数と数の間に+を入れられるようにする
    # ★ step2 文字列にした数の長さを取り、インデックスで+をいれる場所を指定できるようにする。
    # ★ step3 再帰関数を用いて、+が入れられる場所を、+をいれる/入れない時で全通り調べる
    # ★ step4 数と数の間に+を入れてできる数式の和を返す

    #整数値を文字列にする
    str_num = str(num)
    #文字列にした数字の長さを取る
    len_str_num = len(str_num)

    #idxがlen_str_numの文字列のインデックス, sentenceが+と数値を含む文字列
    def dfs(idx: int , sentence: str, str_num: str, len_str_num: int) -> int: 

        # 文字列idxが一番後ろに到達したかどうかを判定
        if idx == len_str_num - 1:
            #+で挟んでいるところで数字をわけ、数値に変更し合計値を出す
            return sum(list(map(int, sentence.split("+"))))
        #間に+を入れるか入れないかで分岐させ、全通り検索できるようにする
        #最終的に佐伯関数からreturnした値を足算していく
        return (
                dfs(idx + 1, sentence + "+" + str_num[idx + 1], str_num, len_str_num) 
              + dfs(idx + 1, sentence + str_num[idx + 1], str_num, len_str_num) 
        )
     
    #初期値として文字列の最初のインデックス, 文字列にした数値の0行目の値, 
    return dfs(0, str_num[0], str_num, len_str_num)

N = int(input())
print(solve_many_formulas(N))
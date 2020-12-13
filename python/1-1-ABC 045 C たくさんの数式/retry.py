# N = int(input())


#ポイント　全文検索　→　文字列のインデックスをとり、間に入れるかどうかで分岐させる。

def sum_all(N: int) -> int:

    str_num = str(N)
    len_str_num = len(str_num)

    def dfs(idx: int, sentence: str):
        
        #インデックスが最大に達した時に終了
        if idx == len_str_num - 1:
            return sum(list(map(int, sentence.split("+"))))
        
        return dfs(idx + 1,sentence + "+" + str_num[idx + 1] ) + dfs(idx + 1, sentence + str_num[idx + 1])

    return dfs(0, str_num[0])

print(sum_all(1234))
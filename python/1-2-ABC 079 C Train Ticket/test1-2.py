def train_ticket(num: int) -> int :

    str_num = str(num)

    #idxが数の文字列のインデックス, formulaが7になった際の出力する式, sum_valが式の合計値
    def dfs(idx, formula, sum_val):

    #インデックスが最大になった時
        if idx == 3:
            if sum_val == 7:
                print(formula + "=7")
                exit()
        else:
            dfs(idx + 1, formula+"+"+str_num[idx + 1], sum_val + int(str_num[idx + 1]))
            dfs(idx + 1, formula+"-"+str_num[idx + 1], sum_val - int(str_num[idx + 1]))
    
    return dfs(0, str_num[0], int(str_num[0]))


print(train_ticket(3242))


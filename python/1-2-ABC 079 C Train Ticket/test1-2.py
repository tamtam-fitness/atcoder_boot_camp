def train_ticket(num: int) -> int :

    str_num = str(num)

    #iがlen_str_num内に入れられる+の場所, formulaが7になった際の出力する式, sum_valが式の合計値
    def dfs(i, formula, sum_val):

       #入れられる数がマックスに達した時
        if i == 3:
            if sum_val == 7:
                print(formula + "=7")
                exit()
        else:
            dfs(i + 1, formula+"+"+str_num[i + 1], sum_val + int(str_num[i + 1]))
            dfs(i + 1, formula+"-"+str_num[i + 1], sum_val - int(str_num[i + 1]))

    return dfs(0, str_num[0], int(str_num[0]))


print(train_ticket(3242))


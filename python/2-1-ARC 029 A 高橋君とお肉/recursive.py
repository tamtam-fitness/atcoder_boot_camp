N = int(input())

meat_time_list = [int(input()) for i in range(N) ]

all_list = []


def dfs(meat_time_idx: int, gril_a: int, gril_b: int):

    global meat_time_list
    global all_list
    
    #idx が lenと同じになるとidxが範囲外となるので、処理を終了さセル
    if meat_time_idx == len(meat_time_list):
        return all_list.append(max(gril_a, gril_b))
    else:
        dfs(meat_time_idx + 1 , gril_a + meat_time_list[meat_time_idx], gril_b) 
        dfs(meat_time_idx + 1 , gril_a, gril_b + meat_time_list[meat_time_idx]) 
    
dfs(0, 0, 0)
print(all_list, min(all_list))

    
        
    

    
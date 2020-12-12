N = int(input())
meat_time_list = []
for _ in range(N):
  meat_time_list.append(int(input()))
  
# 4, 3 ,2 ,1 降順
sorted_meat_time_li = sorted(meat_time_list, reverse = 1)

#初期値の設定
gril_a = [0]
gril_b = [0]

for meat_time in sorted_meat_time_li:
  if sum(gril_a) >= sum(gril_b) :
    gril_b.append(meat_time)
  else :
    gril_a.append(meat_time)
print(max(sum(gril_a), sum(gril_b)))
print(gril_a, gril_b)
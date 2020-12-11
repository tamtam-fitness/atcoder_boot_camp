import random
import time

ques_list = [1, 2, 3]

太田 = "太田"
梶村 = "梶村"
田村 = "田村"

players = [太田, 梶村, 田村]

print("アルゴリズム問題を解説する人を選びます!")
time.sleep(1)
for idx in range(len(players)) :
    x = random.choice(ques_list)
    ques_list.remove(x)
    print(players[idx], x)



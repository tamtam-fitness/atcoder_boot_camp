# 長さ Lの鉄の棒が東西方向
# 11箇所で切断して、12本

# 13
# 2 1 1 1 1 1・・・
# 1 2 1 1 1 1・・・
# 1 1 2 1 1 1・・・

# 切り方がわかればそこからパーミネーションで行けそう。

# 12本で分割する。
 

# 12 / 12
# input

# # modを使ってあまりを出すはどう？？

# L = int(input())

# surplus

# 3

# 1 1 1
# 1 2
# 3

# 5 

# 4 1


# L = int(input())

# surplus = L - 12

# if surplus == 0:
#     print(1)
#     exit()

# print(12 ** surplus)

# from scipy.special import comb


from scipy.special import comb
 
L = int(input())
print(int(comb(L, 11)))
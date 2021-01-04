pockets = 1000
amount_of_shopping = int(input())

cal_exchange = pockets - amount_of_shopping

counts = 0
#デカイ順から並べるのがミソ
for coin in [500, 100, 50, 10, 5, 1] :

    tmp_counts, tmp_exchage = divmod(cal_exchange, coin)

    counts += tmp_counts
    cal_exchange = tmp_exchage

    if cal_exchange == 0:
        break

print(counts)
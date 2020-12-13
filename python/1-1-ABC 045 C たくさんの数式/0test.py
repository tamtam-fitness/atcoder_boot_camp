#num: 等差数列の和で用いる最大の数をいれる 
def sum_all(num: int) -> int:

    if num < 1:
        return num
    return sum_all(num - 1) + num


print(sum_all(10))
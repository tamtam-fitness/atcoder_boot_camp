#n　が　n 番目の数　-->> return に n番目の値を出力
# def fibonacci(n: int) -> int:

#     if (n == 1 or n == 2):
#         return 1
    
#     return fibonacci(n - 2) + fibonacci(n - 1) 
# print(fibonacci(5))

memo = {1:1, 2:1}
def fibonacci(n: int) -> int:

    global memo

    if n in memo :
        return memo[n]
    
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)

    return memo[n]

print(fibonacci(5))

def fib(n):
    results = list(range(n + 1))  # 用于缓存以往结果，以便复用（目标2）

    for i in range(n + 1):  # 按顺序从小往大算（目标3）
        if i < 2:
            results[i] = i
        else:
            # 使用状态转移方程（目标1），同时复用以往结果（目标2）
            results[i] = results[i - 1] + results[i - 2]

    return results[-1]

def f_bad(n):
    if n < 2:
        return n
    else:
        return f_bad(n-1) + f_bad(n-2)



if __name__ == '__main__':
    n=2

    print(f'fib({n})={fib(n)}, f_bad({n})={f_bad(n)}')
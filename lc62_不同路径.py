class Solution:
    # m是行数，n是列数
    def uniquePaths(self, m: int, n: int) -> int:
        results = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                    results[i][j] = results[i-1][j] + results[i][j-1]


        return results[-1][-1]

# m是行数，n是列数
def f(m, n):

    results = [[1] * n] * m

    for i in range(1, m):
        for j in range(1, n):
                results[i][j] = results[i-1][j] + results[i][j-1]

    return results[-1][-1]

if __name__ == '__main__':

    r = f(7, 3)
    print(r)
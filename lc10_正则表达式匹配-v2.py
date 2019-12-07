def f(pattern, i_p, string, i_s, results):
    # 当前是星号
    if pattern[i_p] == '*':
        m_ij = pattern[i_p-1] == string[i_s] or pattern[i_p-1] == '.'
        r = results[i_p - 2][i_s] | results[i_p - 1][i_s] | results[i_p][i_s - 1] & m_ij

    # 当前不是星号
    else:
        m_ij = pattern[i_p] == string[i_s] or pattern[i_p] == '.'
        r = results[i_p - 1][i_s - 1] & m_ij

    return r



def is_match(string, pattern):
    # 初始化二维数组
    len_string = len(string) + 1  # 给二维数组加哨兵，所以+1
    len_pattern = len(pattern) + 1
    results = [[False] * len_string for i in range(len_pattern)]
    results[0][0] = True
    pattern = '_' + pattern  # 兼容哨兵
    string = '_' + string

    # 异常处理
    if len_pattern == len_string == 1:
        return True
    if len_pattern == 1:
        return False
    if pattern[0] == '*':
        return False

    for i_p in range(1, len_pattern):

        if pattern[i_p] == '*':
            results[i_p][0] = results[i_p - 2][0]

        for i_s in range(1, len_string):
            results[i_p][i_s] = f(pattern, i_p, string, i_s, results)


    return results[-1][-1]


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return is_match(s, p)

if __name__ == '__main__':
    s = "aa"
    p = "a*"  # false
    s = "ab"
    p = ".*"  # false
    s = "aab"
    p = "c*a*b" # false
    S = Solution()
    r = S.isMatch(s, p)
    print(r)
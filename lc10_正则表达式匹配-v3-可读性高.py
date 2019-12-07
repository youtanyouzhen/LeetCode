
# 状态转移函数（目标1）
def f(pattern, i, string, j, results):
    # 当前是星号
    if pattern[i] == '*':
        m_ij = pattern[i - 1] == string[j] or pattern[i - 1] == '.'
        r = results[i - 2][j] | results[i - 1][j] | results[i][j - 1] & m_ij

    # 当前不是星号
    else:
        m_ij = pattern[i] == string[j] or pattern[i] == '.'
        r = results[i - 1][j - 1] & m_ij

    return r


# 主匹配函数
def is_match(string, pattern):

    # 初始化二维数组（目标2）
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

    # 外循环遍历pattern（目标3）
    for i in range(1, len_pattern):

        # 这里是哨兵处理相关（与星号的情况1相关）
        if pattern[i] == '*':
            results[i][0] = results[i - 2][0]

        # 内循环遍历string（目标3）
        for j in range(1, len_string):
            # 状态转移函数（目标1），以及复用中间结果（目标2）
            results[i][j] = f(pattern, i, string, j, results)


    return results[-1][-1]


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return is_match(s, p)





if __name__ == '__main__':
    s = "aab"
    p = "c*a*b" # true
    s = "abcd"
    p = "d*"    # false
    s = "aa"
    p = "a*"    # true
    s = "ab"
    p = ".*"    # true
    s = "mississippi"
    p = "mis*is*p*."   # false
    s = "aa"
    p = "a"  # false
    s = "aa"
    p = ""   # false
    s="bbbba"
    p=".*a*a"  # true
    s="aa"
    p = "a*"  #true
    s="aaa"
    p="aaaa"   # false
    s=""
    p=".*"   # true

    S = Solution()
    r = S.isMatch(s, p)
    print(r)
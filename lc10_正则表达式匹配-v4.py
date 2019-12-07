class Solution:




    def isMatch(self, s: str, p: str) -> bool:

        # 初始化二维数组
        s_len = len(s) + 1   # 给二维数组加哨兵，所以+1
        p_len = len(p) + 1
        results = [[False] * (s_len) for i in range(p_len)]
        results[0][0] = True
        p = '_' + p     # 兼容哨兵
        s = '_' + s

        # 异常处理
        if p_len == s_len == 1:
            return True
        if p_len == 1:
            return False
        if p[0] == '*':
            return False


        for i_p in range(1, p_len):


            if p[i_p] == '*':
                results[i_p] = results[i_p - 2]

            for i_s in range(1, s_len):
                # 当前是星号
                if p[i_p] == '*':
                    m_ij = p[i_p-1] == s[i_s] or p[i_p-1] == '.'
                    results[i_p][i_s] |= results[i_p - 1][i_s] | results[i_p][i_s - 1] & m_ij

                # 当前不是星号
                else:
                    m_ij = p[i_p] == s[i_s] or p[i_p] == '.'
                    results[i_p][i_s] |= results[i_p - 1][i_s - 1] & m_ij

        return results[-1][-1]

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
    # s="aa"
    # p = "a*"  #true
    # s="aaa"
    # p="aaaa"   # false
    # s=""
    # p=".*"   # true
    s="aaa"
    p="ab*ac*a"  # true

    S = Solution()
    r = S.isMatch(s, p)
    print(r)
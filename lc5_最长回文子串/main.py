'''
时间复杂度：O(n^2)
空间复杂度：O(1)
'''

class Solution:

    def find_result_odd(self, s, c, max_id):
        max_offset = min(c, max_id-c)
        start = end = c
        for i in range(1, max_offset+1):
            start_tmp = c - i
            end_tmp = c + i
            if s[start_tmp] != s[end_tmp]:
                break
            else:
                start = start_tmp
                end = end_tmp

        return end-start, start, end

    def find_result_even(self, s, c, max_id):
        max_offset = min(c+1, max_id-c)
        start, end = c, c
        for i in range(max_offset):
            start_tmp = c - i
            end_tmp = c + i + 1
            pass
            if s[start_tmp] != s[end_tmp]:
                break
            else:
                start = start_tmp
                end = end_tmp

        return end - start, start, end

    def longestPalindrome(self, s: str) -> str:


        result = dict(
            centre=0,
            start=0,
            end=0
        )
        max_l = 0
        L = len(s)
        for i in range(L):
            # 奇数情况
            l, start, end = self.find_result_odd(s, i, L - 1)
            if l > max_l:
                max_l = l
                result['centre'] = i
                result['start'] = start
                result['end'] = end

            # 偶数情况
            l, start, end = self.find_result_even(s, i, L - 1)
            if l > max_l:
                max_l = l
                result['centre'] = i
                result['start'] = start
                result['end'] = end

        r = s[result['start']:result['end']+1]
        return r

if __name__ == '__main__':
    S = Solution()
    r = S.longestPalindrome("cbbd")
    print(r)
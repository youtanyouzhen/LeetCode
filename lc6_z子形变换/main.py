import math

'''
时间复杂度：O(n)
空间复杂度：O(n)

逐行访问，内嵌逐列访问
两个元素的间隔按行（6,0）,(4, 2)....(0, 6)
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        L = len(s)

        if numRows==1:
            return s
        else:
            groupSize = maxInterval = 2*numRows-2
        groupnum = math.ceil(L/groupSize)

        interval_L = maxInterval
        interval_R = 0
        new_s = ''
        for i in range(numRows):
            new_i = i
            if new_i >= L:
                break
            new_s += s[new_i]
            for j in range(groupnum):

                if interval_L > 0:
                    new_i = new_i + interval_L
                    if new_i >= L:
                        break
                    new_s += s[new_i]

                if interval_R > 0:
                    new_i = new_i + interval_R
                    if new_i >= L:
                        break
                    new_s += s[new_i]

            interval_L -= 2
            interval_R += 2

        return new_s

if __name__ == '__main__':
    S = Solution()
    r = S.convert("Lidfhbidfb", numRows = 1)
    print(r)



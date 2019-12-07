is_digit = lambda x: '0' <= x <= '9'
is_minus = lambda x: x == '-'

class Solution:
    def myAtoi(self, str: str) -> int:

        # 滤掉无用的字符
        stack = []
        for s in str:
            if not stack and is_minus(s):
                stack.append(-1)
            elif not stack and  s=='+':
                stack.append(-2)
            elif is_digit(s):
                stack.append(int(s))
            elif not is_digit(s):
                if stack and stack[-1]>=0:
                    break
                elif not stack and s==' ':
                    pass
                else:
                    return 0
                # if stack:
                #     # 不是负号
                #     if stack[-1]>0:
                #         break
                #     # 去掉负号
                #     stack.pop()

        # 转成数字
        sign=1
        y = 0
        for d in stack:
            if d==-1:
                sign = -1
            elif d==-2:
                sign = 1
            else:
                y = y*10 + d
        y = sign * y
        if y < -2**31:
            return -2**31
        if y >  2**31-1:
            return 2**31-1

        return y




if __name__ == '__main__':
    S = Solution()
    r = S.myAtoi( "- 234")
    print(r)
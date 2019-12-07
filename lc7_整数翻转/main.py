class Solution:
    def reverse(self, x: int) -> int:

        # 记录符号
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        # 入栈
        digits = []
        while x:
            digit = x % 10
            x = int(x / 10)

            digits.append(digit)

        # 合成
        y = 0
        for digit in digits:
            y = y * 10 + digit

        # 溢出处理
        y = sign * y
        if (y > 2 ** 31 - 1) or (y < -2 ** 31):
            return 0

        return y

if __name__ == '__main__':
    S = Solution()
    r = S.reverse(12929)
    print(r)
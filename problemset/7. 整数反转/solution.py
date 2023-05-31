class Solution:
    def reverse(self, x: int) -> int:
        # 定义一个变量存储反转后的结果
        result = 0
        # 定义一个变量存储 x 的符号，1 表示正数，-1 表示负数
        sign = 1 if x >= 0 else -1
        # 将 x 转换为正数，方便处理
        x = abs(x)
        # 循环反转 x 的每一位数字
        while x > 0:
            # 取出 x 的最后一位数字，加到 result 的末尾
            result = result * 10 + x % 10
            # 去掉 x 的最后一位数字
            x = x // 10
        # 恢复 x 的符号，并检查结果是否在范围内
        result = sign * result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result
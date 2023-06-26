class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_all = n * (n + 1) // 2
        for x in range(1, n + 1):
            sum_1_to_x = x * (x + 1) // 2
            sum_x_to_n = sum_all - sum_1_to_x + x
            if sum_1_to_x == sum_x_to_n:
                return x
        return -1
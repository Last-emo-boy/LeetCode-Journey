class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数不是回文数
        if x < 0:
            return False
        if 0 < x < 9:
            return True
        # 回文检查
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False
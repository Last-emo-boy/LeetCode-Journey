class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        
        if not s:
            return 0

        num = 0
        is_negative = False

        if s[0] in ['-', '+']:
            if s[0] == '-':
                is_negative = True
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        num = -num if is_negative else num
        num = max(-2**31, num)
        num = min(2**31 - 1, num)

        # 返回结果
        return num
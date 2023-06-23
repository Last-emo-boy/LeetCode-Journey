class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            # 如果字符串全为数字
            if s.isdigit():
                # 将字符串转化为整数并更新最大值
                max_val = max(max_val, int(s))
            else:
                # 否则，以字符串的长度作为值并更新最大值
                max_val = max(max_val, len(s))
        return max_val。
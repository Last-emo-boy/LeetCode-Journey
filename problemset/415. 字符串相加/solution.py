class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res.append(tmp % 10)
            i, j = i - 1, j - 1
        return ''.join(str(x) for x in res[::-1])
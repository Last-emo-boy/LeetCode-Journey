class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        temp_1 = str(n)
        flag_1 = temp_1 == temp_1[::-1]
        temp_2 = str(bin(n))
        flag_2 = temp_2 == temp_2[::-1]
        
        if flag_1 and flag_2:
            return True
        else:
            return False
 
# sol = Solution()       
# print(sol.isStrictlyPalindromic(9))
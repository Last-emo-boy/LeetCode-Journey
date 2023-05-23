class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        left = 0
        right = 0
        max_length = 0
        char_set = set()

        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return max_length
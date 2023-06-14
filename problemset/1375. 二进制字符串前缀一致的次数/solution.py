class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxFlip = 0
        prefixCount = 0
        for i, flip in enumerate(flips, 1):
            maxFlip = max(maxFlip, flip)
            if maxFlip == i:
                prefixCount += 1
        return prefixCount
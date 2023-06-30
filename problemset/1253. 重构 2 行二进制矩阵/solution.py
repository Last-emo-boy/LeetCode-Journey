class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        upper_row = [0] * len(colsum)
        lower_row = [0] * len(colsum)
        
        for i in range(len(colsum)):
            if colsum[i] == 2:
                upper_row[i] = lower_row[i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    upper_row[i] = 1
                    upper -= 1
                else:
                    lower_row[i] = 1
                    lower -= 1
        if upper == 0 and lower == 0:
            return [upper_row, lower_row]
        else:
            return []
class Solution(object):
    def oddString(self, words):
        n = len(words[0])
        diff_arrays = [self.calculate_diff_array(word, n) for word in words]
        for i in range(len(words)):
            is_different = True
            for j in range(len(words)):
                if j != i and diff_arrays[j] == diff_arrays[i]:
                    is_different = False
                    break
            if is_different:
                return words[i]

    def calculate_diff_array(self, word, n):
        diff_array = []
        for i in range(1, n):
            diff = ord(word[i]) - ord(word[i - 1])
            diff_array.append(diff)
        return diff_array
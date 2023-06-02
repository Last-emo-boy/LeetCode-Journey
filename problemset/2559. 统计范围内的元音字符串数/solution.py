class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(word: str) -> bool:
            return word[0] in 'aeiou' and word[-1] in 'aeiou'
        is_vowel_word = [is_vowel(word) for word in words]
        return [sum(is_vowel_word[l:r+1]) for l, r in queries]

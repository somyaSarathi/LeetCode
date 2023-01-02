class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0] == word[0].upper():
            return word[1:] == word[1:].upper() or word[1:] == word[1:].lower()
        
        if word[0] == word[0].lower():
            return word == word.lower()

        return False

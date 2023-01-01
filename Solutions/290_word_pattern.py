class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        
        if len(s) != len(pattern):
            return False

        seq = {}
        for i in range(len(pattern)):
            if pattern[i] not in seq:
                if s[i] in seq.values():
                    return False
                    
                seq[ pattern[i] ] = s[i]
                continue
            
            if seq[ pattern[i] ] != s[i]:
                return False

        return True

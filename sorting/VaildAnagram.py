class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        str_s = ''.join(sorted(s))
        str_t = ''.join(sorted(t))

        return str_s == str_t
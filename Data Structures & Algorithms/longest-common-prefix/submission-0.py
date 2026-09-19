class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        k = 0

        while k < len(strs[0]):
            for i in range(1, n):
                if k >= len(strs[i]) or strs[i][k] != strs[0][k]:
                    return strs[0][:k]

            k += 1

        return strs[0][:k]
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0
        common = ""

        while length <= len(strs[0]):
            prefixes = [s[:length] for s in strs]
            all_same = all(prefix == prefixes[0] for prefix in prefixes)

            if all_same:
                common = prefixes[0]

            length += 1

        return common
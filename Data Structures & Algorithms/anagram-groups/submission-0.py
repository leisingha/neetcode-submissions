class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            if "".join(sorted(string)) in groups:
                groups["".join(sorted(string))].append(string)
            else:
                groups["".join(sorted(string))] = [string]
        return list(groups.values())

        
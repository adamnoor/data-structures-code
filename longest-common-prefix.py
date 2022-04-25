class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common = strs[0]
        for element in strs:
            if len(element) == 0:
                return ""
            elif len(element) < len(common):
                common = element
        for element in strs:  
            c = ""
            for i in range(0, len(common)):
                if element[i] == common[i]:
                    c = c + common[i]
                else:
                    break
            if len(c) < len(common):
                common = c             
        return common

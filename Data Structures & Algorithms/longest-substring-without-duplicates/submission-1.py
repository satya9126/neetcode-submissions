class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        l = 0
        n = len(s)
        ans=0
        for r in range(n):
            if s[r] not in x:
                x.add(s[r])
            else:
                while s[r] in x:
                    x.remove(s[l])
                    l+=1
                x.add(s[r])
            ans=max(ans,r-l+1)
        return ans
            


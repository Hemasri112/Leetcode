class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        s1=set()
        ans=0
        for right in range(len(s)):
            while s[right] in s1:
                s1.remove(s[left])
                left+=1
            s1.add(s[right])
            ans=max(ans,len(s1))
            right+=1
        return ans
            
        
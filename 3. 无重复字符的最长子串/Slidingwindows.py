class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        charindex={}
        start=0
        for i,x in enumerate(s):
            if x in charindex:
                start=max(charindex[x]+1,start)
            charindex[x]=i
            maxlen=max(maxlen,i-start+1)
        return maxlen
        
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
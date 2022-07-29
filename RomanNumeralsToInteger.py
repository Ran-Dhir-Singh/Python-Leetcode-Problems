class Solution:
    # def romanToInt(self, s: str) -> int:
    #     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    #     i = 0
    #     num = 0
    #     while i < len(s):
    #         if i+1<len(s) and s[i:i+2] in roman:
    #             num+=roman[s[i:i+2]]
    #             i+=2
    #         else:
    #             num+=roman[s[i]]
    #             i+=1
    #     return num

    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        num = roman[s[len(s)-1]]
        for i in range(len(s)-2,-1,-1):
            if roman[s[i]]<roman[s[i+1]]:
                num-= roman[s[i]]


            else:
                num += roman[s[i]]
        return num

s = Solution()
print(s.romanToInt("MCMXCIV"))
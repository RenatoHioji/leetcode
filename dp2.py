class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == 0:
            return 0
        n = len(s)
        prev = 1
        current = 1
        
        for i in range(1, n):
            #Skippa o 1, pois ele vai ser sempre 1
            temp = 0
            if s[i] != '0':
                temp += current
            
            two_digit = int(s [i-1:i+1])
            
            if 10 <= two_digit <= 26:
                temp += prev
            
            prev = current
            current = temp
            
            if current == 0:
                return 0
            
        return current

sol = Solution()
print(sol.numDecodings("1234"))

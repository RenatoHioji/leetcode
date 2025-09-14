from typing import List
##problemas de permutação
class Solution:
    def letterCombination(self, digits: List[str]) -> List[str]:
        ## Mapeamento dos dígitos em letras
        letras = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        if not digits:
            return []
        
        res = []
        
        
        def bt(letrasAgrupadas, digits):
            if not digits:
                res.append(letrasAgrupadas)
                return
            
            for digit in letras[digits[0]]:
                bt(letrasAgrupadas+digit, digits[1:])
        bt("", digits)
        return res

sol = Solution()
print(sol.letterCombination("345"))
from typing import List
class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount+1) # Setando o valor inicial de todos como infinito e setando o tamanho como amount + 1
        arr[0] = 0 # Setando o valor inicial como 0
        for coin in coins: # Para camada moeda na lista de moedas
            for i in range(coin, amount + 1): #Nós vamos pegar a moeda e verificar o 
                arr[i] = min(arr[i], arr[i-coin] + 1) 
        
        return arr[amount] if arr[amount] != float('inf') else -1
    

sol = Solution()

print(sol.coinChange([1, 2, 3], 5))
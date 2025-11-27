class Solution:
    def countBits(self, n: int) -> list[int]:
        memo = [-1 for _ in range(n + 1)]
        memo[0] = 0
        memo[1] = 1

        result = []
        power = 1
        
        for i in range(n + 1):
            if memo[i] != -1: result.append(memo[i])
            else:
                nearest_power = 2 ** power
                if (nearest_power > i): 
                    nearest_power = 2 ** (power)
                    memo[i] = 1 + memo[nearest_power - i]
                elif (nearest_power < i):
                    nearest_power = 2 ** (power)
                    memo[i] = 1 + memo[nearest_power - i]
                else:
                    power == i
                    memo[i] = 1
                result.append(memo[i])
        return result
    

print(Solution.countBits(1, 10))
                


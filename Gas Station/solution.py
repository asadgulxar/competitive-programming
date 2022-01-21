# Problem link : https://leetcode.com/problems/gas-station/submissions/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == len(cost):
            startingStation= 0
            totalFuel = 0
            tank = 0
            for i in range(len(gas)):
                tank = tank + gas[i] - cost[i]
                if tank < 0:
                    startingStation=i+1
                    totalFuel = totalFuel +tank
                    tank = 0
            if totalFuel+tank<0:
                return -1
            else:
                return startingStation
# Two City Scheduling
# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
# A function to return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = {0:[], 1:[]}
        a = 0
        b = 0
        total = 0
        for cost in costs:
            if cost[0] < cost[1]:
                diff[0].append(abs(cost[0] - cost[1]))
                a += 1
            elif cost[0] > cost[1]:
                diff[1].append(abs(cost[0] - cost[1]))
                b += 1
            else:
                a += 1
                b += 1
            total += min(cost)
        
        if a+b > len(costs):
            if a > b:
                a -= 1
            if a < b:
                b -= 1
            
        if a == b:
            return total
        
        if a < b:
            tmp = sorted(diff[1])
            i = 0
            while(a < b):
                total += abs(tmp[i])
                i += 1
                a += 1
                b -= 1
            return total
                
        if a > b:
            tmp = sorted(diff[0])
            i = 0
            while(a > b):
                total += abs(tmp[i])
                i += 1
                b += 1
                a -= 1
            return total

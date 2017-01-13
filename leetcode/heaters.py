import math

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(houses) == 0 or len(heaters) == 0:
            return 0

        if heaters[0] != 1:
            heaters.insert(0, houses[0] - heaters[0] + 1)
        end = heaters[len(heaters) - 1]
        end_house = houses[len(houses) - 1]
        if end < end_house:
            heaters.append(end_house - end + end_house)

        radius = 0
        print(heaters)
        for i in range(1, len(heaters)):
            heater_range = heaters[i] - math.ceil((heaters[i] + heaters[i -1])/ 2.0)
            if heater_range > radius:
                radius = heater_range
        return int(radius)
houses = [1,2,3,5,15]
heaters = [2, 30]

print('radius', Solution().findRadius(houses, heaters))
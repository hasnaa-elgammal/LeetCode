class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearestpoint = []
        nearestdistance = -1
        for point in points:
            if point[0] ==x or point[1] ==y:
                distance = abs(x - point[0]) + abs(y - point[1])
                if nearestdistance == -1 or distance < nearestdistance:
                    nearestdistance = distance
                    nearestpoint = point
                
        if nearestdistance == -1:
            return -1
        else:
            return points.index(nearestpoint)
                
                
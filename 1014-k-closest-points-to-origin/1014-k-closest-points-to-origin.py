import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for i in range(len(points)):
            x1=points[i][0]
            y1=points[i][1]
            euclidean=(x1**2)+(y1**2)
            distances.append(euclidean**2)
        h=[]
        for i in range(len(points)):
            h.append((distances[i],points[i]))
        heapq.heapify(h)
        ans=[]
        for i in range(k):
            dist,point=heapq.heappop(h)
            ans.append(point)
        return ans


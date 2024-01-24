class Twitter:

    def __init__(self):
        self.graph=collections.defaultdict(set)
        self.posts=collections.defaultdict(list)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time,tweetId])
        self.time=self.time-1
        print(self.posts)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        h=[]
        self.graph[userId].add(userId)
        for user in self.graph[userId]:
            for post in self.posts[user]:
                heapq.heappush(h,post) 
        while h and len(res)<10:
            time,curr=heapq.heappop(h)
            res.append(abs(curr))
        return res
        



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
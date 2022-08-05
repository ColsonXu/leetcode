from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


    def getNewsFeed(self, userId):
        res = []
        heap = []

        self.followMap[userId].add(userId)
        for x in self.followMap[userId]:
            if x in self.tweetMap:
                index = len(self.tweetMap[x]) - 1
                count, tweetId = self.tweetMap[x][index]
                heapq.heappush(heap, [count, tweetId, x, index - 1])

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])
        return res
        

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId) -> None:
        self.followMap[followerId].remove(followeeId)

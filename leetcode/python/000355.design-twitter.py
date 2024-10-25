import heapq
from collections import defaultdict


class TwitterHeap:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    # Time complexity: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    # Time complexity: O
    def getNewsFeed(self, userId: int) -> list[int]:
        possibleTweets = []

        for followeeId in self.followMap[userId]:
            for tweet in self.tweetMap[followeeId][-10:]:
                possibleTweets.append(tweet)
        for tweet in self.tweetMap[userId][-10:]:
            possibleTweets.append(tweet)

        # O(n) where n is amount of followers
        # it is faster that adding in heap in each time (n(log(n)))
        heapq.heapify(possibleTweets)

        # O(1) because we need log(n) and n is always 10
        feed = [id for _, id in heapq.nlargest(10, possibleTweets)]
        return feed

    # Time complexity: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    # Time complexity: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followMap[followerId]
        if followeeId in followees:
            followees.remove(followeeId)


class Twitter:
    # Space complexity: O(u + t)
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = []

    # Time complexity: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append({"tweetId": tweetId, "userId": userId})

    # Time complexity: O(u * t)
    def getNewsFeed(self, userId: int) -> list[int]:
        ret = []
        for i in range(len(self.tweets) - 1, -1, -1):
            data = self.tweets[i]
            print(data)
            if data["userId"] == userId or data["userId"] in self.follows[userId]:
                ret.append(data["tweetId"])
            if len(ret) == 10:
                return ret
        return ret

    # Time complexity: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    # Time complexity: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.follows[followerId]
        if followeeId in followees:
            followees.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

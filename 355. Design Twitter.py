class Twitter(object):

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)       # userId -> [(time, tweetId)]
        self.following = defaultdict(set)     # followerId -> {followeeIds}
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        maxHeap = []

        # Ensure user follows themselves
        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if self.tweets[followee]:
                time, tweetId = self.tweets[followee][-1]
                index = len(self.tweets[followee]) - 1
                heapq.heappush(maxHeap, (-time, tweetId, followee, index))

        while maxHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Move to the next older tweet from same followee
            if index > 0:
                nextTime, nextTweetId = self.tweets[followee][index - 1]
                heapq.heappush(maxHeap, (-nextTime, nextTweetId, followee, index - 1))

        return res

        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
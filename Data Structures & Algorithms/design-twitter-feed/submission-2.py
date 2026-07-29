import heapq

class Twitter:

    def __init__(self):
        self.follow_lists = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.time, tweetId))
        else:
            self.tweets[userId] = [(self.time, tweetId)]
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        out = []
        if userId not in self.follow_lists:
            self.follow_lists[userId] = set([userId])
        else:
            self.follow_lists[userId].add(userId)

        for user in self.follow_lists[userId]:
            if user not in self.tweets:
                continue
            if len(self.tweets[user]) < 10:
                h += self.tweets[user]
            else:
                h += self.tweets[user][-10:]
        
        heapq.heapify(h)
        for i in range(10):
            if not h:
                break
            out.append(heapq.heappop(h)[1])
        
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_lists:
            self.follow_lists[followerId].add(followeeId)
        else:
            self.follow_lists[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_lists and followeeId in self.follow_lists[followerId]:
            self.follow_lists[followerId].remove(followeeId)

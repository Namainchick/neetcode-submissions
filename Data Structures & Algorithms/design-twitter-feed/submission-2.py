"""
very high level we need to store:
- user following (should be fast readable and editable)
- posts with priority. in this case time. (heap)
"""

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = []
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts,(-self.time,userId,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = self.posts.copy()
        out = []
        while temp and len(out) < 10:
            _,uid,tid = heapq.heappop(temp)
            if uid in self.follows[userId] or uid == userId:
                out.append(tid)
        return out 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

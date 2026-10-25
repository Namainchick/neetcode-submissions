class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        in the end we want to go from begin to end while using the least steps.
        going from one to another is defined so we can build a directed graph out of 
        this. With a bfs we can then find either the shortest path or that there is no 
        solution. 
        The difficult thing is to build the graph. just blindly checkin each with each 
        takes n^2 but also checking each character takes m if thats length of character.
        One thing i notices is that we never have to go back. With that information we 
        dont find the word we start with the next wave. why this is efficient is if wave 
        2 found a neigbour sag no other wave 2 candidate needs to check that anymore 
        becuase it wont get faster that that. 
        Problem is if the path is as long as the list we have to check the rest for each 
        wave which could still be O(n^2*m)
        Maybe there is a way to do some work but never have to check m for each
        2 words. 
        kann man ein subset zweier listen in O(1) berechnen denn wirbrauchen nur die 
        länge davon. 
        """

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        word_map = {}
        for word in wordList:
            word_map[word] = set()

        word_map[beginWord] = set()

        for word in word_map:
            for i in range(len(word)):
                for a in alphabet:
                    word_map[word].add(word[:i]+a+word[i+1:])
        
        seen = set()
        q = deque([(beginWord,1)])

        while q:
            cur_word,wave = q.popleft()
            if cur_word in seen:
                continue
            seen.add(cur_word)
            candidates = set()
            for i in range(len(cur_word)):
                for a in alphabet:
                    if cur_word[:i]+a+cur_word[i+1:] in wordList:
                        q.append((i,wave+1))
        
            if cur_word == endWord:
                return wave

        return 0
            


        
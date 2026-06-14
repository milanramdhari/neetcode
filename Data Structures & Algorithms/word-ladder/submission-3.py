class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # create graph
        graph = {}
        graph[beginWord] = []
        graph[endWord] = []

        if endWord not in wordList:
            return 0

        def checkValidNeigh(word1, word2):
            firstDiffFound = False
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if firstDiffFound:
                        return False
                    firstDiffFound = True
            return True

        for word in wordList:
            graph[word] = [] 


        for word in wordList:
            check = checkValidNeigh(beginWord, word)
            if check:
                graph[beginWord].append(word)
                graph[word].append(beginWord)

        for word in wordList:
            check = checkValidNeigh(endWord, word)
            if check:
                graph[endWord].append(word)
                graph[word].append(endWord)
        
        if not graph.get(endWord):
            return 0
        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                check = checkValidNeigh(wordList[i], wordList[j])
                if check:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        print(graph)

        q = deque()
        q.append(beginWord)
        res = 0
        visited = set()
        visited.add(beginWord)

        while q:
            print(q)
            level_len = len(q)
            for i in range(level_len):
                curr = q.popleft()
                if curr == endWord:
                    print(curr)
                    return (res + 1)

                for neigh in graph[curr]:
                    if neigh in visited:
                        continue
                    q.append(neigh)
                    visited.add(neigh)
            res += 1
        
        return 0




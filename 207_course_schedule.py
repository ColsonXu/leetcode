from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prereq):
        graph = defaultdict(list)
        for a, b in prereq:
            graph[a].append(b)

        seen = set()
        def dfs(curr):
            if curr in seen:
                return False
            if graph[curr] == []:
                return True

            seen.add(curr)

            for pre in graph[curr]:
                if not dfs(pre):
                    return False

            seen.remove(curr)
            graph[curr] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

import graphlib
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prereq):
        map = defaultdict(list)
        for x in prereq:
            pre = x[0]
            cls = x[1]
            map[pre].append(cls)
        
        ts = graphlib.TopologicalSorter(map)
        try:
            print(tuple(ts.static_order()))
            return True
        except:
            return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = defaultdict(list)
        
        for course, pre in prerequisites:
            prevMap[course].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if prevMap[course] == []:
                return True
            
            visit.add(course)
            for pre in prevMap[course]:
                if not dfs(pre): return False
            visit.remove(course)
            prevMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
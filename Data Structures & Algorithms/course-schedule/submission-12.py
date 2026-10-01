class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for c in pre_map[crs]:
                if dfs(c) is False:
                    return False
            visiting.remove(crs)
            visited.add(crs)

            return True
        
        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True
        
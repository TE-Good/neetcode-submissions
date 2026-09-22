class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()
        visited = set()

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True

            visiting.add(c)
            for p in pre_map[c]:
                if dfs(p) is False:
                    return False
            visiting.remove(c)
            visited.add(c)

            return True

        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True
        
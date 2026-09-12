class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = {crs:[] for crs in range(numCourses)}
        for crs, req in prerequisites:
            pre_reqs[crs].append(req)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for pre_req in pre_reqs[crs]:
                if dfs(pre_req) is False:
                    return False
            visiting.remove(crs)
            visited.add(crs)

            return True
        
        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True
        
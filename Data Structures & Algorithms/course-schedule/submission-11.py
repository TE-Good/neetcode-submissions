class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for req in pre_map[course]:
                if dfs(req) is False:
                    return False
            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if dfs(course) is False:
                return False
        return True

        
        
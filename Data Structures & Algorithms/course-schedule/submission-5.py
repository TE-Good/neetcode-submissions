class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        current_path = set()
        finished = set()

        def dfs(crs):
            if crs in current_path:
                return False
            if crs in finished:
                return True

            current_path.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            current_path.remove(crs)
            finished.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
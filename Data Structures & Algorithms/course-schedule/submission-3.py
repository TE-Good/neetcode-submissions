class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visted_set = set()

        def dfs(crs):
            if crs in visted_set:
                return False
            if pre_map[crs] == []:
                return True

            visted_set.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visted_set.remove(crs)
            pre_map[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                
            
        
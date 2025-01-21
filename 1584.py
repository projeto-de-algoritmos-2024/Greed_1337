class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, rank, x, y):
            px, py = find(parent, x), find(parent, y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        n = len(points)
        edges = []
        

        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))
        

        edges.sort()
 
        parent = list(range(n))
        rank = [0] * n
        
        total_cost = 0
        edges_used = 0
        
        for weight, u, v in edges:
            if union(parent, rank, u, v):
                total_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return total_cost
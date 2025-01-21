class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def process_edges(edges_to_process, uf_alice, uf_bob, is_type3=False):
            count = 0
            for t, u, v in edges_to_process:
                if is_type3:
                    if uf_alice.union(u, v):
                        uf_bob.union(u, v)
                        count += 1
                else:
                    count += (uf_alice.union(u, v) if t == 1 else uf_bob.union(u, v))
            return count
        
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size + 1))
                self.rank = [0] * (size + 1)
                self.components = size
                
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                    
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                    
                self.components -= 1
                return True
                
            def is_connected(self):
                return self.components == 1
        
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        
        type3_edges = [edge for edge in edges if edge[0] == 3]
        other_edges = [edge for edge in edges if edge[0] != 3]
        
        essential_edges = process_edges(type3_edges, alice_uf, bob_uf, True)
        
        essential_edges += process_edges(other_edges, alice_uf, bob_uf)
        
        if alice_uf.is_connected() and bob_uf.is_connected():
            return len(edges) - essential_edges
            
        return -1
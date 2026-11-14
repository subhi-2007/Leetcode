class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for a, b in zip(s, t):
            if s_map.get(a, b) != b or t_map.get(b, a) != a:
                return False

            s_map[a] = b
            t_map[b] = a

        return True
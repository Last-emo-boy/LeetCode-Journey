from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        x = y = 0
        result = 0
        obs = set(map(tuple, obstacles))
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    if (x + dx[d], y + dy[d]) not in obs:
                        x += dx[d]
                        y += dy[d]
                        result = max(result, x * x + y * y)
                    else:
                        break
        return result
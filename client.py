"""
Autonomous Agent Sutherland-Hodgman Polygon Clipping Skill
Pure Python Standard Library implementation.
"""
from typing import List, Tuple, Dict, Any

class SutherlandHodgman:
    """
    Sutherland-Hodgman polygon clipping algorithm.
    """
    @staticmethod
    def clip(subject_polygon: List[Tuple[float, float]], clip_polygon: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        def inside(cp1, cp2, p):
            return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0]) - 1e-9

        def intersection(cp1, cp2, s, e):
            dc = (cp1[0] - cp2[0], cp1[1] - cp2[1])
            dp = (s[0] - e[0], s[1] - e[1])
            n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
            n2 = s[0] * e[1] - s[1] * e[0]
            denom = dc[0] * dp[1] - dc[1] * dp[0]
            if abs(denom) < 1e-12:
                return s
            n3 = 1.0 / denom
            return ((n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3)

        output_list = list(subject_polygon)
        cp_len = len(clip_polygon)
        for i in range(cp_len):
            cp1 = clip_polygon[i]
            cp2 = clip_polygon[(i + 1) % cp_len]
            input_list = output_list
            output_list = []
            if not input_list:
                break
            s = input_list[-1]
            for e in input_list:
                if inside(cp1, cp2, e):
                    if not inside(cp1, cp2, s):
                        output_list.append(intersection(cp1, cp2, s, e))
                    output_list.append(e)
                elif inside(cp1, cp2, s):
                    output_list.append(intersection(cp1, cp2, s, e))
                s = e
        return [(round(x, 4), round(y, 4)) for x, y in output_list]

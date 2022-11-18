class Solution(object):
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        area_c = max(cx2 - cx1, 0) * max(cy2 - cy1, 0)
        return area_a + area_b - area_c

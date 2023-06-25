class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 找到矩形上离圆心最近的点
        # xClosest 为矩形左右边界与圆心 x 坐标三者中间的值，即圆心如果在矩形内部或者右边界，取圆心 x 坐标，如果在左边界外，取矩形左边界坐标
        # yClosest 同理
        xClosest = max(x1, min(xCenter, x2))
        yClosest = max(y1, min(yCenter, y2))

        # 计算圆心和矩形上离圆心最近的点的距离
        distanceX = xCenter - xClosest
        distanceY = yCenter - yClosest

        # 如果这个距离小于或等于圆的半径，那么就可以说圆和矩形有重叠的部分
        return distanceX * distanceX + distanceY * distanceY <= radius * radius
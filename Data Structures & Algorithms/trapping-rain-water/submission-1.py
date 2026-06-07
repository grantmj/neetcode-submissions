class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        answer = 0
        l, r = 0, len(height) - 1
        LeftMax, RightMax = height[l], height[r]
        while l < r:
            if LeftMax < RightMax:
                l += 1
                LeftMax = max(LeftMax, height[l])
                answer += LeftMax - height[l]
            else:
                r -=1
                RightMax = max(RightMax, height[r])
                answer += RightMax - height[r]

        return answer
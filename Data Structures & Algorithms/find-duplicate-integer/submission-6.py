class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        # print(fast, slow)
        temp = 0
        while True:
            temp = nums[temp]
            slow = nums[slow]
            if slow == temp:
                break
                
        return slow
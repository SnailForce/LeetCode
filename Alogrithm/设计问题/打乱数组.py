class Solution:

    def __init__(self, nums: List[int]):
        self.c = nums[:]
        self.r = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.c = self.r

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.c = self.c.shuffle()

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

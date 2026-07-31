class Solution:
    def twoSum(self, nums, target):
        deck = {}
        for i, num in enumerate(nums):
             needed_card = target - num
             if needed_card in deck:
                  return [deck[needed_card], i]
             deck[num] = i


                   
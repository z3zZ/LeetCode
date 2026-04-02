# find where prices are the lowest and then compare that number to the highest price in the future, 
# if there are no numbers where the price is higher, then check the previous number and see if any numbers in the future are higher.
# Follow this pattern until you are at the first int in the array,
# if the condition of profit is never met in the entire array then print. "Do not buy, there are no current profit margins"



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

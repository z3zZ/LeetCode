#Find 2 numbers in an array that sum the inputted value
#Array = nums (int)
#Target input = target (int)
#Cannot use the same number in an array twice (compared 2 diffent numbers)
#Take the target value 
#Then take the first index of "num"
#Compare the Target value to num
#Search the array for a number that equals the subtraction of our num and target
#If none can be found take the 2nd (1) number in the array and compare the same
#Continue untill either the conditions are met or the program has searched through all elements in the array
#Output the elements that were used
## THIS TOOK 6:13 MINS TO COME UP WITH 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#input array = candidates (distinct int)
#input target value = target (int)
#output all unique combinations in the array that sum to "target" 
#Can use the same number twice but within the final array 
#The same value can be outputed within the array twice similar to multiplcation (e.g 1)
#error handling unless im fine to ONLY account for our test cases.(?)
## Time taken for this solution was 8:54



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
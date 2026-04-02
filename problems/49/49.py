#input array # strs (string)
#output should be a new array that groups all strings that can make eachother with their letters
#if inputted nothing then output nothing
#if no available inputs then return the same array
#101 characters allowed within the array
## This took 4mins 30 to come up with (I dont know what algorithm to use at this point)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
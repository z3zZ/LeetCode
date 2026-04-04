
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
#no clue what an lru is, read wiki later
#positive size capacity? =
#key? meaning it probably has something to do with a hashmap
#if the key exists then return it else return -1
#get and put must run in 0(1) which is perfect as this reassures me its a hashmap
#example shows a hashmap
#i think the example tells me that the cache neutral becomes 2
#and if the neutral is 2 it must equal anove the int value of 2?
#this has to be wrong as there are 2 lrucache.get(1) with differnt returns
#OHH the script puts in order the returned values into "void"
#meaning that when a duplicate appears its put into the cache but cant fit? 
#that would explain the "positive size capacity" as its "overflowing"?
#Stopping now because too confused. Will read the wiki for LRU annd refer to solution logic
##this thought process took 11:28mins

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


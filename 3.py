class Solution:
    def lengthOfLongestSubstring(self, stringy: str) -> int:
        
        leftPointer = 0 # holds the position of the left sliding window index
        maxLength = 0 # holds the max length substring (this is what we return)
        seen = {} # disctionary that holds the char and its last seen index i.e., {'c': 6}
        
        # for rightPointer in range of len(string) -> enumerate returns pairs (int rightPointer, string char)
        for rightPointer, char in enumerate(stringy):
            
            # if we have not seen this character, move the right pointer
            # and check if this current window is larger than our current max
            if char not in seen: 
                maxLength = max(maxLength, rightPointer - leftPointer + 1)
                
            # else, we have seen this character before
            else:
                
                # check if the character is in the current window
                # if it is, we need to move the leftPointer to 
                # the position this char was last seen at + 1
                # (we add one so that we dont include this char in the new bounds)
                if seen[char] >= leftPointer:
                    leftPointer = seen[char] + 1
                
                # else the char is not inside the current window, so we 
                # can simply increase the length of the current window logically
                else:
                    maxLength = max(maxLength, rightPointer - leftPointer)
                
            # no matter what happens above, we need to update the last seen
            # index of this character inside the hashmap
            seen[char] = rightPointer
        
        # return the maxLength substring that was found
        return maxLength
        
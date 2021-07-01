class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # the very optmized solution to this is def tricky; however, 
        # this solution performs quite well all things considered, and
        # is rather easy write
        # the idea is somewhat similar to something like twosum, where we know
        # what we are looking for later in the list when we are at a given word
        # therefore, we can simply calculate what it would take for a given word
        # to have a palindrome pair, and add that to a hashmap. Later, if we see
        # any of these prefix/suffix, we simply append them to the results array
        
        # this makes it easy to associate the index to a given word later
        words = {word: i for i, word in enumerate(words)}
    
        # this stores all of the valid palidromes and is what we return
        res = []
        
        # for each of the words in our input
        for word, k in words.items():
            n = len(word)
            
            # we iterate through n + 1 since we need to consider the empty string
            # also, we ignore this empty string when looking at the suffix section
            # since we will have already considered it in the prefix section before
            for j in range(n + 1):
                
                # identify the current prefix and suffix
                pref, suf = word[:j], word[j:]
                
                # if the current prefix is itself palindromic
                if pref == pref[::-1]:
                    
                    # back is the reverse of the suffix, since this is what we 
                    # would be looking for 
                    back = suf[::-1]
                    
                    # if back is not the entire word and back is in words
                    # we have found a valid pair, so append indexes to res
                    if back != word and back in words:
                        res.append([words[back], k])
                        
                # if j != n, since we dont want duplicates here and if 
                # the suffix itself is palindromic
                if j != n and suf == suf[::-1]:
                    
                    # back is the reverse prefix since this is what we
                    # would be looking for 
                    back = pref[::-1]
                    
                    # if back is not the entire word and back is in words,
                    # we have found a valid pair, so appened indexes to res
                    if back != word and back in words:
                        res.append([k, words[back]])
        
        # lastly, return the valid pairs
        return res
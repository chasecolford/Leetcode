class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #could also call .lower() 
        row1 = [x for x in "QWERTYUIOPqwertyuiop"]
        row2 = [y for y in "ASDFGHJKLasdfghjkl"]
        row3 = [z for z in "ZXCVBNMzxcvbnm"]
        
        res = []
        #loop the words
        for w in words:
            flag = True
            #base case: if w == "" ?
            
            #find what row it starts in
            if w[0] in row1:
                for c in w:
                    if c not in row1:
                        flag = False
                        break
                if flag:
                    res.append(w)
            elif w[0] in row2:
                for c in w:
                    if c not in row2:
                        flag = False
                        break
                if flag:
                    res.append(w)
            elif w[0] in row3:
                for c in w:
                    if c not in row3:
                        flag = False
                        break
                if flag:
                    res.append(w)
        return res
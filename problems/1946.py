class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        """
        More formally, digit d maps to digit change[d]
        To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).
        
        greedy? the left most digit changed is always bigger, so we can just look for the biggest leftmost 
        digit we can make the biggest... then just make the biggest possible with the rest of the close digits
        to the right
        """
        m = {i: change[i] for i in range(len(change))}
        res = []
        i = 0
        flag = True
        done = False
        first = True
        while i < len(num):
            cur = int(num[i])
            
            if first:
                # if we find a location where the value is larger if swap
                if m[cur] > cur and not done:
                    if flag: # this is for the first num we find that would be bigger
                        res.append(m[cur])
                        flag = False
                    else: # else if the previous character was also bigger
                        prev = int(num[i-1])
                        if m[prev] >= prev: # okay, prev was also bigger
                            res.append(m[cur])
                        else: 
                            res.append(cur) # dont forget to append this chars regular value
                            done = True # must be subarray (cont) so we are done
                    first = False

                # else, we just append the vhar
                else: res.append(cur)
                i += 1
                
            else:
                # if we find a location where the value is larger if swap
                if m[cur] >= cur and not done:
                    if flag: # this is for the first num we find that would be bigger
                        res.append(m[cur])
                        flag = False
                    else: # else if the previous character was also bigger
                        prev = int(num[i-1])
                        if m[prev] >= prev: # okay, prev was also bigger
                            res.append(m[cur])
                        else: 
                            res.append(cur) # dont forget to append this chars regular value
                            done = True # must be subarray (cont) so we are done

                # else, we just append the vhar
                else: res.append(cur)
                i += 1
        
        res = [str(x) for x in res]
        res = str(int("".join(res)))
        if res == '0': res = res * len(num)
        return res
               
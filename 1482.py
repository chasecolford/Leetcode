# def minDays(bloomDay, mBouquets, kAdjacent):

#     # we can never make them if we need more than the total flowers
#     if mBouquets * kAdjacent > len(bloomDay): return -1

#     checker = [0] * kAdjacent # this will be what we need for a range to be value (i.e. 0 represents its bloomed)
#     day = 0
    
#     baseCase = max(bloomDay)

#     # the most we could ever wait is the max day in the array
#     while day <= baseCase:

#         # first, check if we can make the bouquets now
#         valid = 0 # track how many bouquets we can make
#         i = 0
#         while i < len(bloomDay):
#             # if we have room to check (minus one since we include i in window)
#             if i + (kAdjacent - 1) < len(bloomDay): 
                
#                 # check a sliding window of size kAdjacent (not -1 here for adjacent since exclusive bound)
#                 # print(bloomDay[i:i+kAdjacent])
#                 if bloomDay[i:i+kAdjacent] == checker:
#                     valid += 1 # increment the count we can make
#                     i += kAdjacent # increment the slider (no overlap)

#                 # else, move the window 1 slot
#                 else:
#                     i += 1

#             # if we dont have room to check
#             else:
#                 break

#             if valid >= mBouquets:
#                 return day

#         # if none of that worked, decrement all of the values by 1
#         # print(bloomDay)
#         for v in range(len(bloomDay)):
#             if bloomDay[v] != 0:
#                 bloomDay[v] -= 1
            
#         # else, incrment the day and try again
#         day += 1

#     # if we exit the above and never returned a valid day, we couldnt make it
#     return -1

def minDays(bloomDay, mBouquets, kAdjacent):
    """
    Step through bloomdays, check if we have room to make this many bouguets
    if we do, find the location of mBouquets pain with the SMALLEST max(kadjacent) values, 
    then return the max of those
    """
    if mBouquets * kAdjacent > len(bloomDay): return -1

    i = 0
    kSmallest = []
    while i < len(bloomDay):

        # if we have room to check (minus one since we include i in window)
        if i + (kAdjacent - 1) < len(bloomDay): 
            
            # check a sliding window of size kAdjacent (not -1 here for adjacent since exclusive bound)

            # if we have none, add this one
            if kSmallest == []:
                kSmallest.append(max(bloomDay[i:i+kAdjacent]))
                i += kAdjacent
            else: 
                # sort them
                kSmallest.sort()

                for j in range(len(kSmallest)):
                    if max(bloomDay[i:i+kAdjacent]) < kSmallest[j]:
                        kSmallest[j] = max(bloomDay[i:i+kAdjacent])
                        break
                i += 1
        else:
            i += 1
                    
    return max(kSmallest)



# expected: 9
print(minDays(bloomDay=[1,10,2,9,3,8,4,7,5,6], mBouquets=4, kAdjacent=2))

#expected 3
print(minDays(bloomDay=[1,10,3,10,2], mBouquets=3, kAdjacent=1))
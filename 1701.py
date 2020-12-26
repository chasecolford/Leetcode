"""
There is a restaurant with a single chef. 
You are given an array customers, where customers[i] = [arrivali, timei]:

arrival[i] is the arrival time of the [i]th customer. 
The arrival times are sorted in non-decreasing order.
time[i] is the time needed to prepare the order of the [i]th customer.
"""
#NOTE:
"""
    1 <= customers.length <= 105
    1 <= arrivali, timei <= 104
    arrivali <= arrivali+1
"""

"""
customers, where customers[i] = [arrival[i], time[i]]:
"""
#NOTE: Since these are non-decreasing, we can just read them in order
# for the wait time of the ith customer, we only need to know when the
# chef finishes i-1, therefore, DP. DP[i] == time the chef finishes the 
# ith customer. The wait time for customer i is:
# max(dp[i-1] - arrivalTime[i], 0) + timeToPrepareOrder[i]
def averageWaitingTime(customers) -> float:
    dp = [0] * len(customers) # hold the time the chef finished cooking the ith customer
    res = [0] * len(customers) # hold the wait time for the ith customer

    # hard code the first value -> this is always the arrival time + time to cook
    dp[0] = customers[0][0] + customers[0][1]
    res[0] = customers[0][1] # the first wait time is always just the cook time

    # print("wait time 0: " + str(res[0]))
    # print("DP 0: " + str(dp[0]))
    # # start at one since we hardcoded the first customer
    for i in range(1, len(customers)):

        # get the arrival time and the time to prepare order
        arrivalTime, timeToPrepareOrder = customers[i][0], customers[i][1]
        # print(arrivalTime, timeToPrepareOrder)

        # the time the chef finishes this order is the time he started it + its cook time,
        # NOTE: this is the max of the current arrival time and the last time chef finished (dp[i-1])
        dp[i] = max(arrivalTime, dp[i-1]) + timeToPrepareOrder
        # print(f'DP {i}: {dp[i]}')

        # the wait time for this customer is either:
        # ONLY the time to prepare order (if the chef was ready to cook when they arrived)
        #       i.e., (dp[i-1] - arrivalTime) < arrivalTime[i]
        # OR (dp[i-1] - arrivalTime) + timeToPrepareOrder if the chef was behind and
        #       working on the previous dish when this customer arrived
        res[i] = max(dp[i-1] - arrivalTime, 0) + timeToPrepareOrder
        # print(f'wait time {i}: {res[i]}')
    
    # return a float of the average
    return sum(res) / len(res)


# # Input: customers = [[1,2],[2,5],[4,3]]
# # expected Output: 5.00000
# print(averageWaitingTime([[1,2],[2,5],[4,3]]))

# # Input: customers = [[5,2],[5,4],[10,3],[20,1]]
# # expected Output: 3.25000
# print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))

# Input: [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
# expected Output: 4.16667
# NOTE: ACTUAL WRONG OUTPUT: 3.50000
# print(averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))

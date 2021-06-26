"""
You are given a binary string binary consisting of only 0's or 1's. 
You can apply each of the following operations any number of times:

    Operation 1: If the number contains the substring "00", 
    you can replace it with "10".
        For example, "00010" -> "10010"
    Operation 2: If the number contains the substring "10", 
    you can replace it with "01".
        For example, "00010" -> "00001"

Return the maximum binary string you can obtain after any number of operations. 
Binary string x is greater than binary string y if x's decimal representation 
is greater than y's decimal representation.
"""
"""#NOTE:
    1 <= binary.length <= 105
    binary consist of '0' and '1'.
"""
#NOTE: TIME LIMIT EXCEEDED during the contest
# after studying the problem more, we can greedily calculate this
def maximumBinaryString(binary: str) -> str:

    #NOTE: concept ->
    # we ignore the leading '1', since these are already in the correct spot
    # next, we always want to bubble up the 0's conceptually, so we take operation 2: 10 -> 01
    # lastly, we want to convert our bubbled 0's into 10 pairs, so we do operation 1: 00 -> 10
    # this idea converges such that there is only 1 '0' in the final answer no matter what
    # thus, we can greedily calculate where this '0' would be based on the location of the first 0
    # and the count of 1s

    # if there are no 0's, we can't make any swaps, so this number is already the maximum
    if '0' not in binary: return binary 

    # find the position of the first '0' and count the 1s found after it
    onesAfterFirstZero = binary.count('1', binary.find('0')) 

    # get the length of the string for easier reference math
    lenOfString = len(binary)

    # we return: '1' * (lenOfString - onesAfterFirstZero - 1) ->
    # plus the ONLY '0' at position lenOfString - onesAfterZero
    # plus '1' * onesAfterFirstZero (all the '1' that get bunched
    #       at the right side after doing step 1)
    return '1' * (lenOfString - onesAfterFirstZero - 1) + '0' + '1' * onesAfterFirstZero

"""
Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
"""
# expected output: "111011"
print(maximumBinaryString("000110"))

"""
Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
"""
# expected output: "01"
print(maximumBinaryString("01"))
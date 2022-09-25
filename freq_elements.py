#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

def freq_elements(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n , c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                print(res)

freq_elements([1,2,3,3,3,4,5,5,5,5,5], 2)
freq_elements([1,2,3,3,3,4,5,5,5,5,5,7,7,7,7,7,7], 3)



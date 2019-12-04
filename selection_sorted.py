'''选择排序
* Author: lil-q
* Date:   2019-11-17
*
* Reference: 
*   https://en.wikipedia.org/wiki/Selection_sort
'''
def selection_sorted(nums):
    size = len(nums)
    for i in range(size-1):
        min_index = i
        for j in range(i, size):
            if nums[j] < nums[min_index]:
               min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
#test
nums=[5,4,3,2,1]
print(selection_sorted(nums))
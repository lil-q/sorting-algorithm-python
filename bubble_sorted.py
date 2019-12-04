'''选择排序
* Author: lil-q
* Date:   2019-11-17
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
*	https://www.cnblogs.com/melon-h/archive/2012/09/20/2694941.html
'''
def bubble_sorted(nums):
    size = len(nums)
    for i in range(size-1):
        for j in range(size-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
#test
nums=[5,4,3,2,1]
print(bubble_sorted(nums))

#最优时间复杂度
def bubble_sorted_op(nums):
    size = len(nums)
    for i in range(size-1):
        didSwap=False
        for j in range(size-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                didSwap=True
        if didSwap==False:
            return
    return nums
#test
nums=[5,4,3,2,1]
print(bubble_sorted_op(nums))
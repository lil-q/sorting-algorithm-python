'''归并排序
* Author: lil-q
* Date:   2019-11-18
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F\
*   #Python%E5%8E%9F%E5%9C%B0%E6%8E%92%E5%BA%8F%E7%89%88%E6%9C%AC
'''
import random
def quick_sorted_inp(nums, first, last):
    if first >= last:
        return
    mid_value = nums[first]
    low = first
    high = last
    while low < high:
        while low < high and nums[high] >= mid_value:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < mid_value:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid_value
    quick_sorted_inp(nums, first, low-1)
    quick_sorted_inp(nums, low+1, last)
# test
# 随机生成大小为size的数组
def genData(size):
    MAX = 99997
    nums = [0] * size
    for i in range(size):
        nums[i] = random.randrange(0, MAX)
    return nums


# 验证nums是否真的排好序了
def isSorted(nums):
    sortednums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != sortednums[i]:
            return False
    return True


if __name__ == '__main__':
    for size in range(0, 100):
        nums = genData(size)
        #nums=quick_sorted(nums)
        quick_sorted_inp(nums,0,len(nums)-1)
        if not isSorted(nums):
            print('Fail at size = {0}'.format(size+1),nums)
        else:
            print('Good at size = {0}'.format(size+1))
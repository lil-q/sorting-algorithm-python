'''堆
* Author: lil-q
* Date:   2019-11-17
*
* Reference: 
*   https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/pai-xu-by-powcai-2/
'''
import random
def heap_sorted(nums):
    # 调整最大堆         
    def adjust_heap(idx, max_len):
        left = 2 * idx + 1
        right = 2 * idx + 2
        max_loc = idx
        if left < max_len and nums[max_loc] < nums[left]:
            max_loc = left
        if right < max_len and nums[max_loc] < nums[right]:
            max_loc = right
        if max_loc != idx:
            nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
            adjust_heap(max_loc, max_len)  
    # 建堆
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        adjust_heap(i, n)
    # 排序
    for i in range(1, n):
        nums[0], nums[-i] = nums[-i], nums[0]
        adjust_heap(0, n - i)
    return nums
# test
# 随机生成大小为size的数组
def genData(size):
    MAX = 99997
    v = [0] * size
    for i in range(size):
        v[i] = random.randrange(0, MAX)
    return v


# 验证v是否真的排好序了
def isSorted(v):
    sortedV = sorted(v)
    for i in range(len(v)):
        if v[i] != sortedV[i]:
            return False
    return True

if __name__ == '__main__':
    for size in range(0, 100):
        v = genData(size)
        heap_sorted(v)
        if not isSorted(v):
            print('Fail at size = {0}'.format(size+1),v)
        else:
            print('Good at size = {0}'.format(size+1))
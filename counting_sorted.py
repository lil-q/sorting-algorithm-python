'''希尔排序
* Author: lil-q
* Date:   2019-11-18
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F#Python
'''
import random
def counting_sorted(nums):
	maxValue=-1
	for num in nums:
		if num>maxValue:
			maxValue=num
	bucket = [0]*(maxValue+1)
	for num in nums:
		bucket[num]+=1
	index=0
	for i in range(len(bucket)):
		while bucket[i]>0:
			nums[index] = i
			index+=1
			bucket[i]-=1
	return nums
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
        counting_sorted(nums)
        if not isSorted(nums):
            print('Fail at size = {0}'.format(size+1),nums)
        else:
            print('Good at size = {0}'.format(size+1))
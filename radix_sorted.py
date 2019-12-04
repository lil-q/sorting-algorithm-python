'''基数排序
* Author: lil-q
* Date:   2019-11-18
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F#Python
*   https://www.cnblogs.com/onepixel/p/7674659.html
'''
import random
def radix_sorted(nums):
	maxValue=-1
	for num in nums:
		if num>maxValue:
			maxValue=num 
	# 求最高位数n
	n=len(str(maxValue))
	# 进行n次排序
	for k in range(n):       
		s=[[] for i in range(10)]
		for i in nums:
			s[i//(10**k)%10].append(i)
		nums=[a for b in s for a in b]
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
        nums=radix_sorted(nums)
        if not isSorted(nums):
            print('Fail at size = {0}'.format(size+1),nums)
        else:
            print('Good at size = {0}'.format(size+1))

'''归并排序
* Author: lil-q
* Date:   2019-11-18
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
*	https://blog.csdn.net/Jacketinsysu/article/details/52472364
'''
import random

# 递归法（Top-down）
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
# test
nums=[5,4,3,2,1]
print(merge_sort(nums))

# 迭代法（Bottom-up）

# 生成器产生2的幂
def powerOfTwo(max):
	x=1
	while x<=max:
		yield x
		x*=2

def merge_iter(nums,l1,l2,r2):
	r1=l2-1
	while r1>=l1 and r2>=l2:
		if nums[r1]>nums[r2]:
			tmp=nums[r2]
			nums[r2]=nums[r1]
			tmp_r1=r1-1
			while nums[tmp_r1]>tmp and tmp_r1>=l1:
				nums[tmp_r1+1]=nums[tmp_r1]
				tmp_r1-=1
			nums[tmp_r1+1]=tmp
		r2-=1

# 方法一：用生成器产生1，2，4，8...
def merge_sorted_iter(nums):
	sortedList=[]
	n=len(nums)
	for i in powerOfTwo(n):
	 	for j in range(0,n,i*2):
	 		merge_iter(nums,j,min(j+i,n-1),min(j+2*i-1,n-1))
	return nums

# 方法二：用位操作产生1，2，4，8...
def msi(nums):
	length = len(nums)
	step = 1
    # 步长为1,2,4,8，...，一直合并下去
	while step <= length:
		offset = step << 1
		for index in range(0, length, offset):
			merge_iter(nums, index, min(index+step, length-1), min(index+offset-1, length-1))
		step = offset

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
        # 你可以换成msi()测试
        merge_sorted_iter(nums)
        if not isSorted(nums):
            print('Fail at size = {0}'.format(size+1),nums)
        else:
            print('Good at size = {0}'.format(size+1))
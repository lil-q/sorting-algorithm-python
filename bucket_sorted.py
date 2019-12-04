'''基数排序
* Author: lil-q
* Date:   2019-11-18
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E6%A1%B6%E6%8E%92%E5%BA%8F
*   https://www.cnblogs.com/onepixel/p/7674659.html
'''
import random
def bucket_sorted(nums):
	if not nums:return nums
	maxValue=nums[0]
	minValue=nums[0]
	for num in nums:
		if num>maxValue:
			maxValue=num 
		elif num<minValue:
			minValue=num
	# 将数据映射到桶中
	bucketSize=100 # 设定桶的大小
	bucketCount=(maxValue-minValue)//bucketSize+1 # 计算桶的数量
	buckets=[[] for _ in range(bucketCount)]
	for num in nums:
		buckets[(num-minValue)//bucketSize].append(num)
	# 对桶内排序，这里使用插入排序，也可以递归桶排序。
	res=[]
	for k in buckets:       
		res=res+insertion_sorted(k)
	return res
# 插入排序
def insertion_sorted(nums):
	size = len(nums)
	for i in range(1,size):
		cur_num=nums[i]
		pre_index=i-1

		while nums[pre_index]>cur_num and pre_index>=0:
			nums[pre_index+1]=nums[pre_index]
			pre_index-=1
		nums[pre_index+1]=cur_num
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
        nums=bucket_sorted(nums)
        if not isSorted(nums):
            print('Fail at size = {0}'.format(size+1),nums)
        else:
            print('Good at size = {0}'.format(size+1))

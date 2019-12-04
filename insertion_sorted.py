'''插入排序
* Author: lil-q
* Date:   2019-11-17
*
* Reference: 
*   https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
*	https://www.cnblogs.com/melon-h/archive/2012/09/20/2694941.html
'''
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
#test
nums=[5,4,3,2,1]
print(insertion_sorted(nums))


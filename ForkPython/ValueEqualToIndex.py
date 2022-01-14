	def valueEqualToIndex(self,arr, n):
		# code here
		nums = []
		for i in range (n):
		    if(arr[i]==(i+1)):
		        nums.append(i+1)
		return nums

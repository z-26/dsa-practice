#Brute Force
def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

print(two_sums(nums=[1,2,4,5,3,7], target=9))


# Optimal solution
def two_sum_optimal(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
print(two_sum_optimal(nums=[1,2,3,5,6,7,8], target=10))
def removeDuplicates(nums) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i+1

print(removeDuplicates(nums=[1,1,2,2,3,3,4,4]))
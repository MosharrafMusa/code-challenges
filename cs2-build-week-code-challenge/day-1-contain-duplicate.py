# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# USING LIST.COUNT -- RUNTIME O(N)
def containDuplicate(nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False


nums = [1, 2, 3, 4, 1]
print(containDuplicate(nums))


# USING SET - runtime O(logn)
def containDuplicate_2(nums):
    myset = set()
    for i in nums:
        if i in myset:
            return True
        else:
            myset.add(i)
    return False


nums = [1, 2, 3, 4, 1]
print(containDuplicate_2(nums))
nums = [1, 2, 3, 4]
print(containDuplicate_2(nums))

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def two_sum_1(array, target):
    '''for each elements in array, if target is equal to the said element and another element in the array without the first element
    result is the indeces of the first element and that other element'''
    
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(i, '&', j)

def two_sum_2(nums: list[int], target: int)->list[int]:
    ''' have two version of nums, one mutable and other immutable.
    if diff between target and an element(x) in (call the element y) nums is in the list without x, 
    indices of x & y is the result'''
    
    nums = tuple(nums)
    for n in nums:
        newnums = list(nums)
        newnums.remove(n)
        if target - n in newnums:
            print(target-n)
            return [nums.index(n), nums.index(target - n)]
                
if __name__=='__main__':
    array = [4,5,8,99,6,7,9,8, 90]
    target = 16

    find_res(array, target)

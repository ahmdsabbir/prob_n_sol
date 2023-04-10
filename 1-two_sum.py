# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def find_res(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(i, '&', j)

if __name__=='__main__':
    array = [4,5,8,99,6,7,9,8, 90]
    target = 16

    find_res(array, target)
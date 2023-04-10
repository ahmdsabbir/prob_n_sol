# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def find_res(array, target):
    result = []
    for elem in array:
        loc = array.index(elem)
        for n_elem in array[loc+1:]:
            if elem + n_elem == target:
                return array.index(elem), array.index(n_elem)
                result.append(array.index(elem), array.index(n_elem))

if __name__=='__main__':
    array = [4,5,8,99,6,7,9,90]
    target = 94

    print(find_res(array, target))
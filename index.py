
from statistics import median


def findNumbersThatOccurOnce(nums):
    """
    :param nums:
    :return:
    """
    nums = [1,2,1,3]
    result = []
    for num in nums:
        if nums.count(num) == 1:
            result.append(num)

    print(result)
    return result   

#findNumbersThatOccurOnce([1,2,1,3])


def longer_side(a,b):
    """
    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b

def movingTotal(nums,i):
    """
    :param nums:
    :return:
    """
    total = 0
    for num in nums:
        total += num
        if(i==total):
            return True
    return False
        

''' test movingTotal() '''  
print(movingTotal([1,2,3,4],8))

def append(self, numbers):
    """
    :param numbers: (list) The list of numbers.
    """
    nn = self+numbers
    return nn

print (append([1,2,3,4],[5]))
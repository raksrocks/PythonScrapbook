#Q: Write a method to print even numbers in a list.
#A: 
def   printEvenNumbers(nums):
    """
    :param nums: (list) The list of numbers.
    """
    for num in nums:
        if num % 2 == 0:
            print(num)

print(printEvenNumbers([1,2,3,4,5,6,7,8,9]))

def returnEvenNUmber(nums):
    """
    :param nums: (list) The list of numbers.
    """
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

assert(returnEvenNUmber([1,2,3,4,5,6,7,8,9]), [2,4,6,8])

## Auto Genetrated code by github copilot
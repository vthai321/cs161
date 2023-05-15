"""
Implement Binary Search and understand why it works
Takes in a sorted list, outputs item you're looking for
Divide and conquer: constantly discards half of the list that does not contain desired value


This method does not need to apply to an existing list; you can modify this algorithm to work on problems without lists
You don't explicitely need array, one example is trying to find square root of 64; find a random value in the middle to start with
"""

array = [1,2,2,2,2,2,2,2,2,2] 
target = 2

class findIndex:

    def binarySearch(self, array, target):
        # returns the index that corresponds to target value

        # find the middle element
        left, right = 0, len(array) - 1
        
        while (left <= right):
            midIndex = (left + right) // 2
            if array[midIndex] == target:
                return midIndex
            elif array[midIndex] > target:
                right = midIndex - 1
            else:
                left = midIndex + 1

    def condition(value):
        pass 

    def bin_search_func(array):
        left = 0
        right = len(array) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                right = mid
            else:
                left = mid + 1


searcher = findIndex()
print(searcher.binarySearch(, target))






class findIndex:

    # k is xy cool if k is divisible by x or y or both(think discrete math)
    # this one works


    def condition(self, value, x, y):
        return (value % x == 0 or value % y == 0)

    def cool_xy(self, n, x, y):
        # x and y are relatively prime numbers
        # compute the nth xy cool number (x and/or y is a factor of this number)
        # O(log n + log x + log y) efficiency (divide the list)

        # think about bounds index wise
        
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] (middle number is 8)

        left, right = 1, n * max(x,y) # can't possibly have nth number be larger than n times the max``

        while left <= right:
            mid = (left + right) // 2
            value = (mid // x) + (mid // y) - (mid // (x*y)) # which number are we in the divisible by x or y sequence? Think of indexing, subtract double count
            if value < n:
                left = mid + 1
            else:
                right = mid - 1
        return left # at this point you've zoned in on the proper term 
    """
    def bin_search_func(array):
        left = 0
        right = len(array) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                right = mid
            else:
                left = mid + 1
    """

searcher = findIndex()
#print(searcher.cool_xy(4, 3, 7))
#print(searcher.cool_xy(5, 2, 3))
print(searcher.cool_xy(573,967,199))


# 3, 6, 7, 9, 12, 14, 15, 18, 21, 24, 27, 28





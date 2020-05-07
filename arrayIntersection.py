class ArrayIntersection:
    '''returns an array with the common values in both arrays. 
    intersections for the two arrays are defined by the values that are common in both arrays'''

    def arrayIntersection(self, arr1, arr2):

        # turn both arrays into sets
        set1, set2 = set(arr1), set(arr2)

        myarr = []
        if len(set1) > len(set2):
            for x in set2:
                for y in set1:
                    if x == y:
                        myarr.append(x)
        else:
            for x in set1:
                for y in set2:
                    if x == y:
                        myarr.append(x)

        return myarr
        
x = ArrayIntersection()


print(x.arrayIntersection([1, 4, 5], [12, 2, 3, 4, 56]))

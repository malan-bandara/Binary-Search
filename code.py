import sys 

array = [1,3,4,6,8,11,23,27,30]
begin_index = 0
finish_index = len(array)-1
target = int(sys.argv[1])

def validateTarget(target):
    if target >= array[begin_index] and target <= array[finish_index]:
        pass
    else:
        print("Target out of range!")
        sys.exit()
        


#search function
def binarySearch(begin_index, finish_index, target, array):
    #initialize the mid index
    mid = (begin_index+finish_index)//2
    mid_value = array[mid]

    #compare mid_value
    if target == mid_value:
        print (f"The {target} index is {mid}")


    #If the target is larger than the mid_value
    elif target > mid_value:
        begin_index = mid+1
        binarySearch(begin_index,finish_index,target,array)

    #If the target is smaller than the mid_value
    elif target < mid_value:
        finish_index = mid-1
        binarySearch(begin_index,finish_index,target,array)
    else:
        print (f"Target: {target} doesn't exist!")


validateTarget(target)
binarySearch(begin_index, finish_index, target, array)






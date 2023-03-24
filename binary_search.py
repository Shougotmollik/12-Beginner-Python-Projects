
def binarySearch(array, num, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == num:
            return mid

        elif array[mid] < num:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array =input(f"Input the Array Here : ")
num = input(f"Input the finding number to find from the array : ")

result = binarySearch(array, num, 0, len(array)-1)

if result != -1:
    print(f"Element is present at index {result} ")
else:
    print("Not found")
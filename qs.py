import random
def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
        lesser = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

def randomised_quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot_idx = random.randint(0, len(array)-1)
        pivot = array[pivot_idx]
        lesser = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
    return randomised_quick_sort(lesser) + [pivot] + randomised_quick_sort(greater)


# Avg and Best case Time complexity: O(nlogn)
# Worst case Time Complexity: O(n^2)





print(randomised_quick_sort([34, 34, 523, 234, 445, 1, 556, 67, 8]))
    
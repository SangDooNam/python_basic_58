# TODO implement quicksort
def quicksort(list: list, low=0, high=-1) -> list:
    if high == -1:
        high = len(list) - 1
        
    if low < high:
        pi = partition(list, low, high)
        quicksort(list, low, pi -1)
        quicksort(list, pi + 1, high)
        return list

def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] =  list[j], list[i]
    (list[i + 1], list[high]) = (list[high], list[i + 1])
    
    return i + 1

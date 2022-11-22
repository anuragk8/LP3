import random

def quicksort(arr, start, stop):
    if (start < stop):
        pivot = partitionrand(arr, start, stop)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, stop)

def partitionrand(arr, start, stop):
    randpiv = random.randrange(start, stop)
    arr[randpiv], arr[start] = arr[start], arr[randpiv]
    return partition(arr, start, stop)

def partition(arr, start, stop):
    pivot = start
    i = start-1
    j = stop+1

    while True:
        while True:
            i+=1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j-=1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j 
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    array = [9, 4, 7, 3, 8, 6, 1]
    quicksort(array, 0, len(array)-1)
    print(array)
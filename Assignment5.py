import random


def quicksort(arr, start , stop):
	if(start < stop):
		
		pivotindex = partitionrand(arr, start, stop)
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):

	randpivot = random.randrange(start, stop)
	print(arr[randpivot])
	print(list(arr))
	print()
	arr[start], arr[randpivot] = arr[randpivot], arr[start]
#	print(list(arr))
	return partition(arr, start, stop)

def partition(arr,start,stop):
	pivot = start
	i = start + 1
	
	for j in range(start + 1, stop + 1):
		print(arr, arr[i], arr[j])
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
			print(arr, arr[i], arr[j], "if con")
	print()
	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
	print(arr)
	pivot = i - 1
	#print(arr)
	return (pivot)

if __name__ == "__main__":
	array = [10, 7, 8, 9, 1, 5]
	quicksort(array, 0, len(array) - 1)
	print(array)


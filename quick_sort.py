# deterministic
def quick(arr,low,high):
    if(low<high):
        pi=partition(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[10,7,8,9,1,5]
n=len(arr)
print(quick(arr,0,n-1))

# randomized  variable
import random

def quick_sort(arr, low, high):
    if low < high:
        # Get random pivot position
        pi = randomized_partition(arr, low, high)
        # Sort the left and right parts
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def randomized_partition(arr, low, high):
    # Choose a random pivot index between low and high
    rand_pivot = random.randint(low, high)
    # Swap random pivot with the last element
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ---------- Main Program ----------
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

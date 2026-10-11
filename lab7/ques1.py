# Lab Sheet 7 - All Programs Combined

import heapq

# --- QUESTION 1: Implement Heap, Priority Queue & Heap Sort ---
print("=== QUESTION 1: HEAP & PRIORITY QUEUE ===")
min_heap = []
elements = [4, 2, 7, 19, 5]
for x in elements:
    heapq.heappush(min_heap, x)
print("min Heap:", min_heap)
print("priority Queue [minHeap]: ", end="")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")

max_heap = []
for x in elements:
    heapq.heappush(max_heap, -x)
print("\nmax Heap:", [-x for x in max_heap])
print("priority Queue [maxHeap]: ", end="")
while max_heap:
    print(-heapq.heappop(max_heap), end=" ")

def heap_sort(arr):
    heap = []
    for x in arr:
        heapq.heappush(heap, x)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

arr = [5, 2, 8, 1, 3, 7]
print("\nIn original array:", arr)
print("Heap Sort:", heap_sort(arr))


# --- QUESTION 2: Rearrange Array to Maximize Adjacent Sum Difference ---
print("\n=== QUESTION 2: MAXIMIZE ADJACENT SUM DIFFERENCE ===")
def maximize_difference(arr):
    arr.sort()
    n = len(arr)
    result = []
    left = 0
    right = n - 1
    while left <= right:
        if left <= right:
            result.append(arr[left])
            left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1
    result = result[:n]
    best = result
    total = sum(abs(best[i] - best[i-1]) for i in range(1, n))
    return best, total

arr2 = [1, 2, 4, 7]
result, total = maximize_difference(arr2)
print("Rearranged array:", result)
print("maximum sum:", total)


# --- QUESTION 3: Smallest Subarray with Sum Greater Than Target ---
print("\n=== QUESTION 3: SMALLEST SUBARRAY WITH SUM GREATER THAN TARGET ===")
def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')
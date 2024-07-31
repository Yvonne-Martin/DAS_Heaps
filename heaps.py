
#1. Implement a max-heap 
class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []  
    def insert(self, val):
        # Add new element to the end of the heap
        self.heap.append(val)  
        self._heapify_up(len(self.heap) - 1)  

    def extract_max(self):
        if len(self.heap) == 0:
            # Check if heap is empty
            raise IndexError('Extracting from an empty heap')  
        if len(self.heap) == 1:
            # If only one element, remove and return it
            return self.heap.pop()  
        root = self.heap[0] 
        # Replace root with last element
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0) 
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2  
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] 
            self._heapify_up(parent_index)  

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2  
        largest = index  
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            # Update largest if left child is greater
            largest = left_child  
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            # Update largest if right child is greater
            largest = right_child  
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  
            self._heapify_down(largest)  

#2. Implement heap sort to sort an array in ascending
def heap_sort(arr):
    def _heapify_down(i, size):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  
        if left < size and arr[left] > arr[largest]:
            largest = left  # Update largest if left child is greater
        if right < size and arr[right] > arr[largest]:
            largest = right  # Update largest if right child is greater
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap if needed
            _heapify_down(largest, size)  # Continue heapifying down

    size = len(arr)  # Get the size of the array
    for i in range(size // 2 - 1, -1, -1):
        _heapify_down(i, size)  

    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        _heapify_down(0, i)  # Rebuild heap with reduced size

#3. Impelement a priority queue
import heapq

class PriorityQueue:
    def __init__(self):
        # Initialize an empty list to store elements
        self.heap = []  

    def push(self, item, priority):
        # Push item with its priority
        heapq.heappush(self.heap, (priority, item))  

    def pop(self):
        # Pop item with the highest priority
        return heapq.heappop(self.heap)[1]  

    def peek(self):
        # Peek at the item with the highest priority
        return self.heap[0][1] if self.heap else None  
    
#4. Find the K most frequent elements in an array
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count frequency of each element
    count = Counter(nums)  
    # Get K most frequent elements
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]  

#5. Given K sorted linked lists, merge them into one sorted list

import heapq
def merge_k_sorted_lists(lists):
    # Initialize a min-heap
    min_heap = []  
    for i, lst in enumerate(lists):
        if lst:
             # Push the first element of each list
            heapq.heappush(min_heap, (lst[0], i, 0)) 
   # Initialize result list
    result = []  
    while min_heap:
        # Pop the smallest element
        value, list_index, element_index = heapq.heappop(min_heap)  
        result.append(value)  
        if element_index + 1 < len(lists[list_index]):
            heapq.heappush(min_heap, (lists[list_index][element_index + 1], list_index, element_index + 1))  
    return result

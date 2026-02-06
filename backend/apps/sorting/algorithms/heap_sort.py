from ..services.step_tracker import StepTracker

def heap_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n:
            tracker.log_comparison([i, l], arr)
            if arr[l] > arr[largest]:
                largest = l
            
        if r < n:
            tracker.log_comparison([largest, r], arr)
            if arr[r] > arr[largest]:
                largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            tracker.log_swap([i, largest], arr)
            heapify(arr, n, largest)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
        
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        tracker.log_swap([i, 0], array)
        heapify(array, i, 0)
        
    return tracker.finalize(array)

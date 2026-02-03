from ..services.step_tracker import StepTracker

def heap_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        tracker.log_comparison()
        if l < n and arr[i] < arr[l]:
            largest = l
            
        tracker.log_comparison()
        if r < n and arr[largest] < arr[r]:
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            tracker.log_swap()
            tracker.log_step(arr)
            heapify(arr, n, largest)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
        
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        tracker.log_swap()
        tracker.log_step(array)
        heapify(array, i, 0)
        
    return tracker.finalize(array)

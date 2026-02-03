from ..services.step_tracker import StepTracker

def selection_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            tracker.log_comparison()
            if array[j] < array[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            tracker.log_swap()
            tracker.log_step(array)
            
    return tracker.finalize(array)

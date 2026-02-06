from ..services.step_tracker import StepTracker

def selection_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            tracker.log_comparison([j, min_idx], array)
            if array[j] < array[min_idx]:
                min_idx = j
                
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            tracker.log_swap([i, min_idx], array)
            
    return tracker.finalize(array)

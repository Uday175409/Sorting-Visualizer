from ..services.step_tracker import StepTracker

def bubble_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            tracker.log_comparison([j, j + 1], array)
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                tracker.log_swap([j, j + 1], array)
                swapped = True
                
        if not swapped:
            break
            
    return tracker.finalize(array)

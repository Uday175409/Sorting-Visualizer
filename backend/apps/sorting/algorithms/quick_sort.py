from ..services.step_tracker import StepTracker

def quick_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]
        
        # Highlight pivot?
        # tracker.log_step(arr, "Pivot selected at " + str(high))
        
        for j in range(low, high):
            tracker.log_comparison([j, high], arr)
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                tracker.log_swap([i, j], arr)
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        tracker.log_swap([i + 1, high], arr)
        return (i + 1)

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(array, 0, len(array) - 1)
    return tracker.finalize(array)

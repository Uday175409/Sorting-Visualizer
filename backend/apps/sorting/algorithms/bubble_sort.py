from ..services.step_tracker import StepTracker

def bubble_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            tracker.log_comparison()
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                tracker.log_swap()
                tracker.log_step(array)
                swapped = True
                
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return tracker.finalize(array)

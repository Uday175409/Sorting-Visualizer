from ..services.step_tracker import StepTracker

def insertion_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    # Traverse through 1 to len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        # Move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0:
            tracker.log_comparison()
            if array[j] > key:
                array[j + 1] = array[j]
                tracker.log_swap() # Log assignment as a swap/move
                tracker.log_step(array)
                j -= 1
            else:
                break
        
        array[j + 1] = key
        # Only log a step if we actually did something significant effectively,
        # but in insertion sort, placing the key back is part of the flow.
        if j + 1 != i:
             tracker.log_step(array)

    return tracker.finalize(array)

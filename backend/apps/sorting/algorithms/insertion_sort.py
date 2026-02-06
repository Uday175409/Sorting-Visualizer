from ..services.step_tracker import StepTracker

def insertion_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    n = len(array)
    
    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        # We assume comparison with key is effectively comparison with index i (initially)
        # But since key is separate, we highlight j to show we are looking at it.
        
        while j >= 0:
            tracker.log_comparison([j], array)
            if array[j] > key:
                array[j + 1] = array[j]
                tracker.log_overwrite([j + 1], array, array[j])
                j -= 1
            else:
                break
        
        array[j + 1] = key
        tracker.log_overwrite([j + 1], array, key)

    return tracker.finalize(array)

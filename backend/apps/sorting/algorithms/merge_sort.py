from ..services.step_tracker import StepTracker

def merge_sort(array):
    tracker = StepTracker()
    tracker.log_initial_state(array)
    
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        # Create temp arrays
        L = [0] * n1
        R = [0] * n2
        
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
            
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
        
        while i < n1 and j < n2:
            tracker.log_comparison()
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            tracker.log_swap() # Log assignment
            tracker.log_step(arr) # Visualize assignment
            k += 1
            
        # Copy remaining elements of L[]
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            tracker.log_swap()
            tracker.log_step(arr)
            
        # Copy remaining elements of R[]
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            tracker.log_swap()
            tracker.log_step(arr)

    def merge_sort_helper(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_helper(array, 0, len(array) - 1)
    return tracker.finalize(array)

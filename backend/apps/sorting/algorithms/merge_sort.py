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
            # Map temp array logic to original array indices for visualization if possible
            # L[i] originated from l+i
            # R[j] originated from m+1+j
            # Note: The values in arr at these indices might have been overwritten if we were doing in-place, 
            # but here we use temp arrays so arr[k] is being overwritten.
            # Visualizing comparison between "values" is best described.
            tracker.log_comparison([k], arr) # Highlight where we are writing to?
            # Or better, just log description. 
            # Ideally we'd highlight the SOURCE blocks (l..m) and (m+1..r).
            # But let's keep it simple: Compare values at front of L and R.
            # Since L and R are temp, we can't highlight them on the main array chart easily if those slots in main array are being overwritten.
            # However, until we overwrite arr[k], arr[k] holds OLD garbage (or old sorted values).
            # Actually, standard merge sort overwrites.
            
            if L[i] <= R[j]:
                arr[k] = L[i]
                tracker.log_overwrite([k], arr, L[i])
                i += 1
            else:
                arr[k] = R[j]
                tracker.log_overwrite([k], arr, R[j])
                j += 1
            k += 1
            
        while i < n1:
            arr[k] = L[i]
            tracker.log_overwrite([k], arr, L[i])
            i += 1
            k += 1
            
        while j < n2:
            arr[k] = R[j]
            tracker.log_overwrite([k], arr, R[j])
            j += 1
            k += 1

    def merge_sort_helper(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_helper(array, 0, len(array) - 1)
    return tracker.finalize(array)

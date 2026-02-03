import time
import copy

class StepTracker:
    def __init__(self):
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
        self.start_time = time.perf_counter()
        self.initial_array = []

    def log_initial_state(self, array):
        self.initial_array = copy.deepcopy(array)
        self.steps.append(copy.deepcopy(array))

    def log_comparison(self):
        self.comparisons += 1

    def log_swap(self):
        self.swaps += 1

    def log_step(self, array):
        """
        Log the current state of the array.
        Ideally called after a swap or significant modification.
        """
        self.steps.append(copy.deepcopy(array))

    def finalize(self, array):
        """
        Calculate final metrics and return the result dictionary.
        """
        end_time = time.perf_counter()
        execution_time_ms = (end_time - self.start_time) * 1000
        
        # Ensure the final sorted state is recorded last if not already
        if not self.steps or self.steps[-1] != array:
            self.steps.append(copy.deepcopy(array))

        return {
            "steps": self.steps,
            "sorted_array": array,
            "metrics": {
                "comparisons": self.comparisons,
                "swaps": self.swaps,
                "execution_time_ms": round(execution_time_ms, 4)
            }
        }

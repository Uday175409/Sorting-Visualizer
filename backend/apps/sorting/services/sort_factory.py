from ..algorithms.bubble_sort import bubble_sort
from ..algorithms.selection_sort import selection_sort
from ..algorithms.insertion_sort import insertion_sort
from ..algorithms.merge_sort import merge_sort
from ..algorithms.quick_sort import quick_sort
from ..algorithms.heap_sort import heap_sort

ALGORITHM_MAP = {
    'bubble': {
        'func': bubble_sort, 
        'time_complexity': 'O(n^2)', 
        'space_complexity': 'O(1)'
    },
    'selection': {
        'func': selection_sort, 
        'time_complexity': 'O(n^2)', 
        'space_complexity': 'O(1)'
    },
    'insertion': {
        'func': insertion_sort, 
        'time_complexity': 'O(n^2)', 
        'space_complexity': 'O(1)'
    },
    'merge': {
        'func': merge_sort, 
        'time_complexity': 'O(n log n)', 
        'space_complexity': 'O(n)'
    },
    'quick': {
        'func': quick_sort, 
        'time_complexity': 'O(n log n)', 
        'space_complexity': 'O(log n)'
    },
    'heap': {
        'func': heap_sort, 
        'time_complexity': 'O(n log n)', 
        'space_complexity': 'O(1)'
    }
}

class SortFactory:
    @staticmethod
    def sort(algorithm_name, array):
        algo_info = ALGORITHM_MAP.get(algorithm_name.lower())
        if not algo_info:
            raise ValueError(f"Algorithm '{algorithm_name}' not found. Available: {list(ALGORITHM_MAP.keys())}")
        
        result = algo_info['func'](array)
        
        # Add static complexity info to result
        result['complexity'] = {
            'time': algo_info['time_complexity'],
            'space': algo_info['space_complexity']
        }
        return result

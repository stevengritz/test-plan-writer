from typing import List, TypeVar, Any

T = TypeVar('T')

def remove_duplicates(items: List[T]) -> List[T]:
    """Removes duplicate items from a list while preserving order.
    
    Args:
        items: List of items
        
    Returns:
        A new list with duplicates removed
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def find_most_common(items: List[Any]) -> Any:
    """Finds the most frequently occurring item in a list.
    
    Args:
        items: List of items
        
    Returns:
        The most common item
        
    Raises:
        ValueError: If the list is empty
    """
    if not items:
        raise ValueError("Cannot find most common item in empty list")
    
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    
    return max(counts.items(), key=lambda x: x[1])[0]

def merge_sorted_lists(list1: List[T], list2: List[T]) -> List[T]:
    """Merges two sorted lists into a single sorted list.
    
    Args:
        list1: First sorted list
        list2: Second sorted list
        
    Returns:
        A new sorted list containing all elements from both input lists
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def binary_search(items: List[T], target: T) -> int:
    """Performs binary search on a sorted list.
    
    Args:
        items: Sorted list of items
        target: Item to find
        
    Returns:
        Index of the target if found, -1 otherwise
    """
    left, right = 0, len(items) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

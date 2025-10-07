"""
Quicksort Algorithm Implementation in Python

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array
and partitioning the other elements into two sub-arrays, according to whether they are less than or
greater than the pivot. The sub-arrays are then sorted recursively.

Time Complexity:
- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n^2) (when the pivot is the smallest or largest element)

Space Complexity:
- O(log n) due to recursive stack space.

Example Usage:
>>> arr = [10, 7, 8, 9, 1, 5]
>>> quicksort(arr)
[1, 5, 7, 8, 9, 10]
"""

def quicksort(arr):
    """
    Sorts an array in ascending order using the Quicksort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Example usage
    example_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", example_array)
    sorted_array = quicksort(example_array)
    print("Sorted array:", sorted_array)

def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


"""
Swap two elements in a list.

Args:
    list_to_swap: The list containing the elements to swap.
    index_to_swap_from: The index of the first element.
    index_to_swap_with: The index of the second element.

Returns:
    The list with the two elements swapped.
"""


def bubble_sort(array_to_sort: list[int]):
    length = len(array_to_sort)
    did_it_swap = True
    while did_it_swap == True:
        did_it_swap = False

        for index in range(0, length-1):
            element1 = array_to_sort[index]
            element2 = array_to_sort[index+1]
            if element1 > element2:
                print(f'[To Swap] — {element1}, and {element2}')
                array_to_sort = my_swap(array_to_sort, index, index+1)
                did_it_swap = True

        print(f"[End of For Loop]Array looks like this now: {array_to_sort}")
        print(
            f"Does the array still need to be sorted / checked one last time? {did_it_swap}")
    return array_to_sort


"""
Sort a list of integers into ascending order using bubble sort.

The function repeatedly compares adjacent elements and swaps them
when they are in the wrong order. It stops when a complete pass
is made without any swaps.

Args:
    array_to_sort: The list of integers to sort.

Returns:
    The sorted list.
"""


def bubble_sort_variant_amy(array_to_sort: list[int]):
    length = len(array_to_sort)
    while True:
        did_it_swap_this_round = False

        for index in range(0, length-1):
            element1 = array_to_sort[index]
            element2 = array_to_sort[index+1]
            if element1 > element2:
                print(element1, element2)
                array_to_sort = my_swap(array_to_sort, index, index+1)
                did_it_swap_this_round = True
        if did_it_swap_this_round == False:
            break


"""
Sort a list of integers into ascending order using bubble sort.

This version uses a boolean variable to record whether a swap
occurred during each pass and stops when no swaps are needed.

Args:
    array_to_sort: The list of integers to sort.
"""


def main():
    my_list = [2, 10, 14, 5, 9]
    print(f"Unsorted list: {my_list}")
    swapped_list = bubble_sort(array_to_sort=my_list)
    print(f"Sorted list: {swapped_list}")
    amy_swapped_list = bubble_sort_variant_amy(array_to_sort=my_list)
    print(f" Amy sorted list: {amy_swapped_list}")
    print("amy sorted list, " + str(amy_swapped_list))


"""
Run the program and demonstrate the bubble sort algorithm.

Creates an example list, sorts it using the bubble sort function,
and displays the results.
"""

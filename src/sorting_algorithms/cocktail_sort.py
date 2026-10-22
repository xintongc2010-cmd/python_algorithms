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


def cocktail_sort(array_to_sort: list[int]):
    length = len(array_to_sort)
    while True:
        did_it_swap = False

        for index in range(0, length-1):
            element1 = array_to_sort[index]
            element2 = array_to_sort[index+1]

            if element1 > element2:
                array_to_sort = my_swap(array_to_sort, index, index+1)
                did_it_swap = True

        for backward_index in range(length-2, 1, -1):
            element3 = array_to_sort[backward_index+1]
            element4 = array_to_sort[backward_index]

            if element3 < element4:
                array_to_sort = my_swap(
                    array_to_sort, backward_index+1, backward_index)
                did_it_swap = True

        if did_it_swap == False:
            break
    return array_to_sort


"""
Sort a list of integers into ascending order using cocktail sort.

The function repeatedly passes through the list forwards and backwards,
swapping adjacent elements that are in the wrong order. It stops when a
complete cycle is made without any swaps.

Args:
    array_to_sort: The list of integers to sort.

Returns:
    The sorted list.
"""


def main():
    my_list = [3, 100, 1, 2, 4, 5, 6, 7, 8, 9]
    print(f"Unsorted list: {my_list}")
    swapped_list = cocktail_sort(array_to_sort=my_list)
    print(f"Sorted list: {swapped_list}")


main()


"""
Run the program and demonstrate the bubble sort algorithm.

Creates an example list, sorts it using the cocktail sort function,
and displays the results.
"""

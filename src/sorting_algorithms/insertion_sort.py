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


def insertion_sort(list_to_sort: list[int]):
    list_length = len(list_to_sort)

    for index in range(1, list_length):
        index_to_start_from = index

        while index_to_start_from >= 1 and list_to_sort[index_to_start_from - 1] > list_to_sort[index_to_start_from]:
            list_to_sort = my_swap(
                list_to_sort, index_to_start_from, index_to_start_from - 1)
            index_to_start_from -= 1

    return list_to_sort


"""
Sort a list of integers into ascending order using insertion sort.

The function moves through the list from left to right and repeatedly
swaps each element backwards until it is in the correct position.

Args:
    list_to_sort: The list of integers to sort.

Returns:
    The sorted list.
"""


def main():
    my_list = [10, 5, 30, 15, 25, 20]
    print("unsorted list:", my_list)
    swapped_list = insertion_sort(list_to_sort=my_list)
    print("sorted list:", swapped_list)


main()


"""
Run the program and demonstrate the insertion sort algorithm.

Creates an example list, sorts it using the bubble sort function,
and displays the results.
"""

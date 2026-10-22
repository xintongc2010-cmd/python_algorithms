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


def selection_sort(list_to_sort: list[int]):
    length_of_list = len(list_to_sort)

    for current_index in range(length_of_list-1):
        min_value = list_to_sort[current_index]
        min_index = current_index

        for inner_index in range(current_index+1, length_of_list):
            current_value = list_to_sort[inner_index]

            if current_value < min_value:
                min_index = inner_index
                min_value = current_value

        if min_index != current_index:
            list_to_sort = my_swap(list_to_sort, current_index, min_index)

    return list_to_sort


"""
Sort a list of integers into ascending order using selection sort.

The function searches the unsorted part of the list for the smallest
value and swaps it into the next correct position.

Args:
    list_to_sort: The list of integers to sort.

Returns:
    The sorted list.
"""


def main():
    my_list = [10, 5, 30, 15, 25, 20]
    print("unsorted list:", my_list)
    swapped_list = selection_sort(list_to_sort=my_list)
    print("sorted list:", swapped_list)


main()


"""
Run the program and demonstrate the selection sort algorithm.

Creates an example list, sorts it using the bubble sort function,
and displays the results.
"""

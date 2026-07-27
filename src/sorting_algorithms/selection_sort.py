def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


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


def main():
    my_list = [10, 5, 30, 15, 25, 20]
    print("unsorted list:", my_list)
    swapped_list = selection_sort(list_to_sort=my_list)
    print("sorted list:", swapped_list)


main()

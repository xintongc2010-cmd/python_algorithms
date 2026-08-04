def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


def insertion_sort(list_to_sort: list[int]):
    list_length = len(list_to_sort)

    for index in range(1, list_length):
        index_to_start_from = index

        while index_to_start_from >= 1 and list_to_sort[index_to_start_from - 1] > list_to_sort[index_to_start_from]:
            list_to_sort = my_swap(
                list_to_sort, index_to_start_from, index_to_start_from - 1)
            index_to_start_from -= 1

    return list_to_sort


def main():
    my_list = [10, 5, 30, 15, 25, 20]
    print("unsorted list:", my_list)
    swapped_list = insertion_sort(list_to_sort=my_list)
    print("sorted list:", swapped_list)


main()

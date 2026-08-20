def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


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


def main():
    my_list = [3, 100, 1, 2, 4, 5, 6, 7, 8, 9]
    print(f"Unsorted list: {my_list}")
    swapped_list = cocktail_sort(array_to_sort=my_list)
    print(f"Sorted list: {swapped_list}")


main()

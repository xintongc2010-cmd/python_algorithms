'''
def bubble_sort(array_to_sort: list[int]):
    length = len(array_to_sort)
    did_it_swap = True
    while did_it_swap == True:
        did_it_swap = False

        for index in range(0, length-1):
            element1 = array_to_sort[index]
            element2 = array_to_sort[index+1]
            if element1 > element2:
                print(element1, element2)
                array_to_sort = my_swap(array_to_sort, index, index+1)
                did_it_swap = True


def main():
    bubble_sort(array_to_sort=[10, 30, 60])


main()


def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


def main():
    my_list = [20, 10, 30]
    my_new_list = my_swap(my_list, index_to_swap_from=0, index_to_swap_with=1)
    print(my_new_list)


def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap
'''


def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


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


def main():
    my_list = [2, 10, 14, 5, 9]
    print(f"Unsorted list: {my_list}")
    swapped_list = bubble_sort(array_to_sort=my_list)
    print(f"Sorted list: {swapped_list}")
    amy_swapped_list = bubble_sort_variant_amy(array_to_sort=my_list)
    print(f" Amy sorted list: {amy_swapped_list}")
    print("amy sorted list, " + str(amy_swapped_list))

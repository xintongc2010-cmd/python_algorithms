def bubble_sort(array_to_sort: list[int]):
    print(array_to_sort)


'''
def main():
    bubble_sort(array_to_sort=[10, 30, 60])


main()
'''


def my_swap(list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
    new_value = list_to_swap[index_to_swap_from]
    list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
    list_to_swap[index_to_swap_with] = new_value
    return list_to_swap


def main():
    my_list = [20, 10, 30]
    my_new_list = my_swap(my_list, index_to_swap_from=0, index_to_swap_with=1)
    print(my_new_list)


main()

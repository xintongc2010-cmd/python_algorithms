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

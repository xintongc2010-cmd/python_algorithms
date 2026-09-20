
class sorting_algorithms:

    def __init__(self, unsorted_list: list[int]) -> None:
        self.unsorted_list = unsorted_list
        self.sorted_list = []

    def my_swap(self, list_to_swap: list[int], index_to_swap_from: int, index_to_swap_with: int):
        new_value = list_to_swap[index_to_swap_from]
        list_to_swap[index_to_swap_from] = list_to_swap[index_to_swap_with]
        list_to_swap[index_to_swap_with] = new_value
        return list_to_swap

    def sorting(self) -> None:
        pass


class bubble_sort(sorting_algorithms):
    def __init__(self, unsorted_list: list[int]):
        super().__init__(unsorted_list)

    def sorting(self):
        list_to_sort = self.unsorted_list.copy()
        length = len(list_to_sort)
        did_it_swap = True
        while did_it_swap == True:
            did_it_swap = False

            for index in range(0, length-1):
                element1 = list_to_sort[index]
                element2 = list_to_sort[index+1]
                if element1 > element2:
                    print(f'[To Swap] — {element1}, and {element2}')
                    list_to_sort = self.my_swap(list_to_sort, index, index+1)
                    did_it_swap = True

            print(
                f"[End of For Loop]Array looks like this now: {list_to_sort}")
            print(
                f"Does the array still need to be sorted / checked one last time? {did_it_swap}")

        self.sorted_list = list_to_sort


class selection_sort(sorting_algorithms):
    def __init__(self, unsorted_list: list[int]):
        super().__init__(unsorted_list)

    def sorting(self):
        list_to_sort = self.unsorted_list.copy()
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
                list_to_sort = self.my_swap(
                    list_to_sort, current_index, min_index)

        self.sorted_list = list_to_sort


class insertion_sort(sorting_algorithms):

    def __init__(self, unsorted_list: list[int]):
        super().__init__(unsorted_list)

    def sorting(self):
        list_to_sort = self.unsorted_list.copy()
        list_length = len(list_to_sort)

        for index in range(1, list_length):
            index_to_start_from = index

            while index_to_start_from >= 1 and list_to_sort[index_to_start_from - 1] > list_to_sort[index_to_start_from]:
                list_to_sort = self.my_swap(
                    list_to_sort, index_to_start_from, index_to_start_from - 1)
                index_to_start_from -= 1

        self.sorted_list = list_to_sort


class cocktail_sort(sorting_algorithms):
    def __init__(self, unsorted_list: list[int]):
        super().__init__(unsorted_list)

    def sorting(self):

        list_to_sort = self.unsorted_list.copy()
        length = len(list_to_sort)
        while True:
            did_it_swap = False

            for index in range(0, length-1):
                element1 = list_to_sort[index]
                element2 = list_to_sort[index+1]

                if element1 > element2:
                    list_to_sort = self.my_swap(list_to_sort, index, index+1)
                    did_it_swap = True

            for backward_index in range(length-2, 1, -1):
                element3 = list_to_sort[backward_index+1]
                element4 = list_to_sort[backward_index]

                if element3 < element4:
                    list_to_sort = self.my_swap(
                        list_to_sort, backward_index+1, backward_index)
                    did_it_swap = True

            if did_it_swap == False:
                break

        self.sorted_list = list_to_sort


def main():
    my_bubble_sort = bubble_sort(unsorted_list=[1, 2, 4, 6, 4, 10])
    my_bubble_sort.sorting()
    print(f"this is bubble sort: {my_bubble_sort.sorted_list}")

    my_selection_sort = selection_sort(unsorted_list=[1, 2, 4, 6, 4, 10])
    my_selection_sort.sorting()
    print(f"this is selection sort: {my_selection_sort.sorted_list}")

    my_insertion_sort = insertion_sort(unsorted_list=[1, 2, 4, 6, 4, 10])
    my_insertion_sort.sorting()
    print(f"this is insertion sort: {my_insertion_sort.sorted_list}")

    my_cocktail_sort = cocktail_sort(unsorted_list=[1, 2, 4, 6, 4, 10])
    my_cocktail_sort.sorting()
    print(f"this is cocktail sort: {my_cocktail_sort.sorted_list}")


main()

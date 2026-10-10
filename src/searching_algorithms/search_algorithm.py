
class searching_algorithms:

    def __init__(self, list_to_search: list[int], target_number: int) -> None:
        self.list_to_search = list_to_search
        self.target_number = target_number
        self.target_index = -1

    def searching(self) -> None:
        pass


class linear_search(searching_algorithms):
    def __init__(self, list_to_search: list[int], target_number: int):
        super().__init__(list_to_search, target_number)

    def searching(self):
        found = False
        index = 0

        while index < len(self.list_to_search) and found == False:

            if self.list_to_search[index] == self.target_number:
                self.target_index = index
                found = True

            else:
                index += 1

        if found == False:
            print("Not found")


class binary_search(searching_algorithms):
    def __init__(self, list_to_search: list[int], target_number: int):
        super().__init__(list_to_search, target_number)

    def searching(self):
        found = False
        lowerBound = 0
        upperBound = len(self.list_to_search) - 1

        while lowerBound <= upperBound and found == False:

            midpoint = (lowerBound + upperBound) // 2

            if self.list_to_search[midpoint] == self.target_number:
                self.target_index = midpoint
                found = True

            elif self.list_to_search[midpoint] > self.target_number:
                upperBound = midpoint - 1

            else:
                lowerBound = midpoint + 1

        if found == False:
            print("Not found")


class jump_search(searching_algorithms):
    def __init__(self, list_to_search: list[int], target_number: int, step: int = 1):
        self.step = step
        super().__init__(list_to_search, target_number)

    def searching(self):
        found = False
        index = 0
        upperBound = len(self.list_to_search) - 1

        while found == False and index <= upperBound:
            new_index = index + self.step

            if self.list_to_search[new_index] == self.target_number:
                self.target_index = new_index
                found = True
                break

            if self.list_to_search[new_index] < self.target_number:
                index += 1
                continue

            for value in range(index, new_index):

                if self.list_to_search[value] == self.target_number:
                    self.target_index = value
                    found = True

            index += 1

        if found == False:
            print("Not found")


def main():
    my_linear_search = linear_search(
        list_to_search=[1, 2, 4, 6, 8, 10], target_number=4)
    my_linear_search.searching()
    print(
        f"[Linear Search] The target number is at index: {my_linear_search.target_index}")

    my_binary_search = binary_search(
        list_to_search=[1, 2, 4, 6, 8, 10], target_number=4)
    my_binary_search.searching()
    print(
        f"[Binary Search] The target number is at index: {my_binary_search.target_index}")

    my_jump_search = jump_search(
        list_to_search=[1, 6, 9, 15, 17, 21, 30, 48, 61, 99], target_number=30, step=3)
    my_jump_search.searching()
    print(
        f"[Jump Search] The target number is at index: {my_jump_search.target_index}")


main()

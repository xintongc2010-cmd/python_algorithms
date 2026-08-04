def main():
    my_list = [10, 5, 30, 15, 25, 20]
    list_length = len(my_list)

    print("list:", my_list)
    print("list_length:", list_length)
    print()

    print("range(1, list_length)  -> indices we visit:")
    for index in range(1, list_length):
        print(f"   index {index} -> value {my_list[index]}")

    print()

    print("range(1, list_length - 1)  -> indices we visit:")
    for index in range(1, list_length):
        print(f"   index {index} -> value {my_list[index]}")


main()

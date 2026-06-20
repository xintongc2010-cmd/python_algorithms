

def my_create():
    array: list[int] = [10, 20, 30, 40, 50]
    print(array)


def my_insert():
    array: list[int] = [10, 20, 30, 40, 50]
    array.insert(0, 50)
    array.insert(1, 4)
    print(array)


def my_remove():
    array: list[int] = [10, 20, 30, 30, 40, 50, ]
    array.remove(30)
    print(array)


def my_update():
    array: list[int] = [10, 20, 30, 40, 50]
    array[1] = 90
    print(array)


def main():
    my_create()
    my_insert()
    my_remove()
    my_update()


main()

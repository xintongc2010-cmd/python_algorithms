def main():
    temperatures = [None] * 31
    temperatures[0] = 15
    print(temperatures[0])


main()


def my_create():
    array = [10, 20, 30, 40, 50]
    print(array)


my_create()


def my_insert():
    array = [10, 20, 30, 40, 50]
    array.insert(0, 50)
    array.insert(1, 4)
    print(array)


my_insert()


def my_remove():
    array = [10, 20, 30, 40, 50]
    array.remove(30)
    print(array)


my_remove()


def my_update():
    array = [10, 20, 30, 40, 50]
    array.update(2, 70)
    print(array)


my_update()

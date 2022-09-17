def FlatIterator(nested_list):
    res = (value for list_ in nested_list for value in list_)
    while True:
        try:
            yield next(res)
        except StopIteration:
            break


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

if __name__ == "__main__":
    print('Задание 1')
    for item in FlatIterator(nested_list):
        print(item)

    print('-' * 20)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list, end='\n\n')

    print('-' * 50)

    print('Задание 2')

    flat_generator = (value for list_ in nested_list for value in list_)
    for item in flat_generator:
        print(item)

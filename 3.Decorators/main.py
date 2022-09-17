import moduls as md


@md.logger
def FlatIterator(nested_list):
    res = (value for list_ in nested_list for value in list_)
    while True:
        try:
            yield next(res)
        except StopIteration:
            break


@md.logger_sign_decorator('log3.txt')
def FlatIterator_(nested_list):
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
    print(list(FlatIterator(nested_list)))
    print('Задание 2')
    print(list(FlatIterator_(nested_list)))

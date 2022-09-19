class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.cursor = 0
        self.step = -1
        return self

    def __next__(self):
        self.step += 1
        if self.step > len(self.list_[self.cursor]) - 1:
            self.cursor += 1
            if self.cursor >= len(self.list_):
                raise StopIteration
            self.step = 0
        return self.list_[self.cursor][self.step]


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

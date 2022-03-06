from task_2 import path_function


nested_list = [
    ['a', [['b'], 'c']],
    ['d', 'e', [[['f']], 'h'], False],
    [1, 2, None]]


@path_function('Protocol', 'log.txt')
def generator(my_list):
    full_list = []

    def recruitment(lists):
        for value in lists:
            if not isinstance(value, list):
                full_list.append(value)
            else:
                recruitment(value)

    recruitment(my_list)
    for i in full_list:
        yield i


if __name__ == '__main__':
    d = generator(nested_list)
    print(list(d))

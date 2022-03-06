import os
import datetime


def path_function(name_folder, name_file, path=os.getcwd()):

    def wrapper(some_function):
        my_list = []
        time = str(datetime.datetime.now())
        path_folder = os.path.join(path, name_folder)
        path_file = os.path.join(path_folder, name_file)
        if not os.path.exists(path):
            os.mkdir(path_folder)

        def new_function(*args, **kwargs):
            if len(args) > 0:
                for i in args:
                    my_list.append(i)
            if len(kwargs) > 0:
                for i, k in kwargs.items():
                    old_str = f'{i}: {k}'
                    my_list.append(old_str)
            result = some_function(*args, **kwargs)
            text = f'{time[:19]} запуск функции "{some_function.__name__}", ' \
                   f'аргументы: {str(my_list)[1:-1]}, значение функции: "{result}"\n'
            with open(path_file, 'at') as file:
                file.write(text)
            return result

        return new_function

    return wrapper

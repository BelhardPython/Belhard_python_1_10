"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows():
    with open('text.txt') as file:
        with open('new_text.txt', 'w') as new_file:
            for line in file:
                temp_list = line.split(' ')
                reverse_string = ' '.join(temp_list[::-1])
                new_file.write(reverse_string)
    return new_file


revert_rows()

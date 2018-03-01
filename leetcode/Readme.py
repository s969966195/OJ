# coding=utf-8
import time
from Config import Config
import os


class Readme(object):
    def __init__(self, total, solved, locked, others=None):
        self.total = total
        self.solved = solved
        self.others = others
        self.locked = locked
        self.msg = 'Completed: **{}** / **{}**\n\n' \
                   'Completed: \n\n' \
                   '| Python | Java | C++ |\n' \
                   '| --- | ---: | :---: |\n' \
                   '| {Python} | {Java} | {C++} |\n\n'.format(self.solved, self.total, self.locked, **self.others)

    def create_leetcode_readme(self, table_instance):
        file_path = os.getcwd() + '/README.md'
        with open(file_path, 'a') as f:
            f.write('## LeetCode\n')
            f.write(self.msg)
            f.write('| ID | Title | Difficulty | Python | Java | C++ |\n')
            f.write('|:---:' * 6 + '|\n')
            table, table_item = table_instance

            for index in table:
                item = table_item[index]
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.id,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'Python': item.python if item.python else 'To Do',
                    'Java': item.java if item.java else 'To Do',
                    'C++': item.c_plus_plus if item.c_plus_plus else 'To Do'
                }
                line = '|{id}|{title}|{difficulty}|{Python}|{Java}|{C++}|\n'.format(**data)
                f.write(line)
        print('leetcode README.md已完成.......')

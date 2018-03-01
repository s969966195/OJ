# coding=utf-8
import time
from Config import Config
import os


class Readme(object):
    def __init__(self, solved, others=None):
        self.solved = solved
        self.others = others
        self.msg = 'Completed: **{}**\n\n' \
                   'Completed: \n\n' \
                   '| Python | Java | C++ |\n' \
                   '| --- | ---: | :---: |\n' \
                   '| {Python} | {Java} | {C++} |\n\n'.format(self.solved, **self.others)

    def create_nowcoder_readme(self, table, subjects):
        file_path = os.getcwd() + '/README.md'

        with open(file_path, 'a') as f:
            f.write(self.msg)
            f.write('\n---------------------\n')
            f.write('## Nowcoder\n')
            for subject in subjects.values():
                f.write('### {}\n'.format(subject))
                f.write('| Title | Python | Java | C++ |\n')
                f.write('|:---:' * 4 + '|\n')

                for item in table:
                    if item.subject == subject:
                        data = {
                            'title': '{}'.format(item.title),
                            'Python': item.python if item.python else 'To Do',
                            'Java': item.java if item.java else 'To Do',
                            'C++': item.c_plus_plus if item.c_plus_plus else 'To Do'
                        }
                        line = '{title}|{Python}|{Java}|{C++}|\n'.format(**data)
                        f.write(line)
        print('nowcoder README.md已完成.......')

# coding=utf-8
from CompleteInform import CompleteInform
import os
from Config import Config
from Question import Question
from Readme import Readme


subjects = {
    '1': '剑指offer'
}


class NowcoderTableInform:
    def __init__(self):
        self.questions = []
        self.table = []

    def update_table(self, oj):
        complete_info = CompleteInform()
        oj_algorithms = os.getcwd() + '/' + oj
        folders = os.listdir(oj_algorithms)
        for folder in folders:
            folder_list = folder.split('.')
            subject = subjects[folder_list[0]]
            title = folder_list[1]
            q = Question(title, subject)
            for _, _, files in os.walk(os.path.join(oj_algorithms, folder)):
                if len(files) != 0:
                    complete_info.complete_num += 1
                for item in files:
                    folder_url = os.path.join(folder, item)
                    folder_url = os.path.join(Config.github_nowcoder_url, folder_url)
                    folder_url = folder_url.replace(' ', '%20')
                    if item.endswith('.py'):
                        complete_info.solved['Python'] += 1
                        q.python = '[Python]({})'.format(folder_url)
                    elif item.endswith('.java'):
                        complete_info.solved['Java'] += 1
                        q.java = '[Java]({})'.format(folder_url)
                    elif item.endswith('.cpp'):
                        complete_info.solved['C++'] += 1
                        q.c_plus_plus = '[C++]({})'.format(folder_url)
            self.table.append(q)

        readme = Readme(complete_info.complete_num, complete_info.solved)
        readme.create_nowcoder_readme(self.table, subjects)
        print complete_info.solved 

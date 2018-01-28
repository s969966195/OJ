# coding=utf-8
import requests
import json
from Question import Question
from CompleteInform import CompleteInform
import os
from Readme import Readme
from Config import Config


class TableInform:
    def __init__(self):
        self.questions = []
        self.table = []
        self.table_item = {}
        self.locked = False

    def get_leetcode_problems(self):
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content

        self.questions = json.loads(content)['stat_status_pairs']

        difficultys = ['Easy', 'Medium', 'Hard']
        for i in range(len(self.questions) - 1, -1, -1):
            question = self.questions[i]
            title = question['stat']['question__title']
            url = question['stat']['question__title_slug']
            id = str(question['stat']['frontend_question_id'])
            if int(id) < 10:
                id = '00' + id
            elif int(id) < 100:
                id = '0' + id
            lock = question['paid_only']
            if lock:
                self.locked = True
            difficulty = difficultys[question['difficulty']['level'] - 1]
            url = Config.leetcode_url + url + '/description/'
            q = Question(id, title, url, lock, difficulty)

            self.table.append(q.id)
            self.table_item[q.id] = q

        return self.table, self.table_item

    def __create_folder(self, oj_name):
        oj_algorithms = os.getcwd() + '/' + oj_name

        if os.path.exists(oj_algorithms):
            print oj_name + ' 文件夹已存在.'
        else:
            print '创建 {} 文件夹......'.format(oj_name)
            os.mkdir(oj_algorithms)

        for item in self.table_item.values():
            question_folder_name = oj_algorithms + '/' + item.id + '. ' + item.title
            if not os.path.exists(question_folder_name):
                print question_folder_name + '文件夹不存在, 正在创建......'
                os.mkdir(question_folder_name)

    def update_table(self, oj):
        complete_info = CompleteInform()
        self.get_leetcode_problems()
        complete_info.total = len(self.table)
        self.__create_folder(oj)
        oj_algorithms = os.getcwd() + '/' + oj
        for _, folders, _ in os.walk(oj_algorithms):
            for folder in folders:
                for _, _, files in os.walk(os.path.join(oj_algorithms, folder)):
                    if len(files) != 0:
                        complete_info.complete_num += 1
                    for item in files:
                        folder_url = folder.replace(' ', '%20')
                        folder_url = os.path.join(folder_url, item)
                        folder_url = os.path.join(Config.github_leetcode_url, folder_url)
                        if item.endswith('.py'):
                            complete_info.solved['Python'] += 1
                            self.table_item[folder[:3]].python = '[Python]({})'.format(folder_url)
                        elif item.endswith('.java'):
                            complete_info.solved['Java'] += 1
                            self.table_item[folder[:3]].java = '[Java]({})'.format(folder_url)
                        elif item.endswith('.cpp'):
                            complete_info.solved['C++'] += 1
                            self.table_item[folder[:3]].c_plus_plus = '[Java]({})'.format(folder_url)

        readme = Readme(complete_info.total,
                        complete_info.complete_num,
                        complete_info.lock,
                        complete_info.solved)
        readme.create_leetcode_readme([self.table, self.table_item])
        print(complete_info.solved)

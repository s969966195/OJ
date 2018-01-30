# coding=utf-8


class Question(object):
    def __init__(self, id, title, url, lock, difficulty):
        self.id = id
        self.title = title
        self.url = url
        self.lock = lock  # boolean，锁住需要购买
        self.difficulty = difficulty

        self.python = ''
        self.java = ''
        self.c_plus_plus = ''

    def __repr__(self):
        return "<id为{}，title为{}，url为{}>".format(str(self.id), str(self.title), str(self.url))

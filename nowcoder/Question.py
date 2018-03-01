# coding=utf-8


class Question(object):
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject

        self.python = ''
        self.java = ''
        self.c_plus_plus = ''

    def __repr__(self):
        return "<title为{}，subject为{}>".format(str(self.title),
                str(self.subject))

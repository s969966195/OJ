# coding=utf-8


class CompleteInform:
    def __init__(self):
        self.solved = {
            'Python': 0,
            'C++': 0,
            'Java': 0,
        }
        self.complete_num = 0
        self.lock = False
        self.total = 0

    def __repr__(self):
        return '<solved: {}>'.format(str(self.solved))

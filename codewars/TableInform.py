# coding=utf-8
import requests
import json


class TableInform:
    def __init__(self):
        self.questions = []
        self.table = []
        self.table_item = {}
        self.locked = False



# -*- coding:utf-8 -*-
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # 正则
        # return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)

        # 自动机
        i = 0
        if s[i] == '+' or s[i] == '-' or s[i].isdigit():
            i += 1
            while s[i] != '\0' and s[i].isdigit():
                i += 1
            if s[i] == '.':
                i += 1
                if s[i].isdigit():
                    i += 1
                    while s[i] != '\0' and s[i].isdigit():
                        i += 1
                    if s[i] == 'e' or s[i] == 'E':
                        i += 1
                        if s[i] == '+' or s[i] == '-' or s[i].isdigit():
                            i += 1
                            while s[i] != '\0' and s[i].isdigit():
                                i += 1
                            if s[i] == '\0':
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif s[i] == '\0':
                        return True
                    else:
                        return False
                elif s[i] == '\0':
                    return True
                else:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                i += 1
                if s[i] == '+' or s[i] == '-' or s[i].isdigit():
                    i += 1
                    while s[i] != '\0' and s[i].isdigit():
                        i += 1
                    if s[i] == '\0':
                        return True
                    else:
                        return False
                else:
                    return False
            elif s[i] == '\0':
                return True
            else:
                return False
        else:
            return False

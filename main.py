# coding=utf-8
from leetcode.TableInform import LeetcodeTableInform
from nowcoder.TableInform import NowcoderTableInform
import time
import os

def init_readme():
    msg = '# OJ\n' \
          'Until {}\n' \
          '\nThis project can make your github tiles look great  (;=_=)\n' \
          '- [LeetCode](#leetcode)\n' \
          '- [NowCoder](#nowcoder)\n'.format(time.strftime("%Y-%m-%d %H:%M:%S",
              time.localtime()))
    file_path = os.getcwd() + '/README.md'
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(msg)
        f.write('\n---------------------\n')

if __name__ == '__main__':
    init_readme()
    print('Readme初始化已完成...')
    leetcode = LeetcodeTableInform()
    leetcode.update_table('leetcode_subjects')
    nowcoder = NowcoderTableInform()
    nowcoder.update_table('nowcoder_subjects')

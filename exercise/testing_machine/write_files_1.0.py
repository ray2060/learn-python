import sys


FILENAME = 'abc'                                                                                            # 文件名与格式
FILE_FORMAT = '.txt'
# 题目可以是多行的
QUESTIONS = ['''你的儿子是否叫胡畔阳？正确打T，错误打F''', '''1+10=20？正确打T，错误打F''']                 # 题目，格式：['''第一题''', '''第二题''', ...]题目可以是多行的
TYPE_OPTIONS = ['T', 'F']                                                                                   # 选项

f = open(FILENAME + FILE_FORMAT, 'w')
user_input = input('\n'.join(QUESTIONS) + '\n请在同一行内写完所有答案\n')
for i in user_input:
    if i not in TYPE_OPTIONS or i == '':
        f.close()
        sys.exit('输入的选项不正确:' + user_input)
f.write(user_input)
f.close()

import random

WEIGHT = [41033, 24137, 14198, 8352, 4912, 2889]

class Student():
    def __init__(self):
        self.w_fact = float(input('input W fact: '))
        self.name = input('input student name: ')
        ts = input(f'input {self.name}\'s will: ').split()
        self.wills = [int(s) for s in ts]
    
    def get_will(self, idx):
        return self.wills[idx]
    
    def get_weight(self, idx):
        return self.w_fact * WEIGHT[idx]
    
    def output(self, idx, sum_idx, student_num):
        res = ''
        res += '-' * 30 + '\n'
        res += f'Student {self.name}:\n'
        res += f'Will #{idx + 1}\n'
        res += f'Seat #{self.wills[idx]}\n'
        res += f'Weight {self.get_weight(idx)}\n'
        res += f'Next fact {self.w_fact ** 0.4 * (idx + 1) / (sum_idx + student_num)}\n'
        return res

student_num = int(input('input student num(recommended less than 7): '))
stu_lst = [Student() for i in range(student_num)]

results = []
max_weight = -1

def solve(depth, wi):
    global max_weight, results, stu_lst, student_num
    if depth >= student_num:
        if len(set([wi[i] for i in range(student_num)])) != student_num:
            return 
        weights = [stu_lst[i].get_weight(wi[i]) for i in range(student_num)]
        if sum(weights) > max_weight:
            results.clear()
            max_weight = sum(weights)
        if sum(weights) >= max_weight:
            results.append(''.join([stu_lst[i].output(wi[i], sum(wi), student_num) for i in range(student_num)]))
        return
    else:
        for i in range(len(stu_lst[depth].wills)):
            solve(depth + 1, wi + [i])

solve(0, [])
random.shuffle(results)
print(('-' * 40 + '\n').join(results))
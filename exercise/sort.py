import random as r
import time as t


def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def bogo_sort(ls):
    ans = ls
    while not is_sorted(ans):
        r.shuffle(ans)
    return ls

def selection_sort(ls):
    for i in range(len(ls) - 1):
        minj = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[minj]:
                minj = j
            if i == minj:
                continue
            ls[i], ls[minj] = ls[minj], ls[i]
    if is_sorted(ls):
        return ls

def bubble_sort(ls):
    for i in range(len(ls), 0, -1):
        for j in range(i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    if is_sorted(ls):
        return ls

def sort(ls, mode=None, return_time=True):
    '''
    mode:
    s(class<str>):selection_sort
    Time complexity:O(n^2)
    Spatial complexity:O(1)
    Is stable:True
    
    None(class<Nonetype>):bogo_sort
    Time complexity:O(n!)
    Spatial complexity:O(n)
    Is stable:False
    
    b(class<str>):bubble_sort
    Time complexity:O(n^2)
    Spatial complexity:O(1)
    Is stable:True
    '''
    
    timer = t.time()
    if mode == 's':
        ans = selection_sort(ls)
    elif mode == 'b':
        ans = bubble_sort(ls)
    elif mode is None:
        ans = bogo_sort(ls)
    if return_time:
        return t.time() - timer, ans
    else:
        return ans
        

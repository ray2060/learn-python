from math import ceil
import os
from colorama import init, Fore, Back, Style
import random

STTPMP = {
    1 : '中毒', 
    2 : '冰冻',
    3 : '震动',
    6 : '回血'
}

SKLPMP = {
    1 : '火球术',
    2 : '冰冻术',
    3 : '施毒术',
    4 : '连击',
    5 : '治愈术',  
    6 : '铁壁', 
    7 : '吸血（弱）', 
    8 : '地震',
    9 : '吸血（强）',
    10 : '群体治愈'
}

SKLCD = {
    0 : {
        1 : 18,
        2 : 25,
        3 : 27,
        4 : 29,
        5 : 37,  
        6 : 31, 
        7 : 17, 
        8 : 42,
        9 : 43,
        10 : 64
    }, 
    1 : {
        1 : 18,
        2 : 25,
        3 : 27,
        4 : 29,
        5 : 18,  
        6 : 15, 
        7 : 17, 
        8 : 42,
        9 : 43,
        10 : 32
    }, 
    2 : {
        1 : 9,
        2 : 25,
        3 : 27,
        4 : 14,
        5 : 37,  
        6 : 31, 
        7 : 17, 
        8 : 42,
        9 : 43,
        10 : 64
    }, 
    3 : {
        1 : 18,
        2 : 25,
        3 : 27,
        4 : 29,
        5 : 37,  
        6 : 31, 
        7 : 8, 
        8 : 42,
        9 : 21,
        10 : 64
    }, 
    4 : {
        1 : 18,
        2 : 12,
        3 : 13,
        4 : 29,
        5 : 37,  
        6 : 31, 
        7 : 17, 
        8 : 42,
        9 : 43,
        10 : 64
    }, 
    5 : {
        1 : 9,
        2 : 25,
        3 : 27,
        4 : 29,
        5 : 37,  
        6 : 31, 
        7 : 17, 
        8 : 21,
        9 : 43,
        10 : 64
    }, 
    6 : {
        1 : 18,
        2 : 25,
        3 : 27,
        4 : 29,
        5 : 37,  
        6 : 15, 
        7 : 17, 
        8 : 1, # 21
        9 : 43,
        10 : 64
    }
}
JOBPMP = {
    1 : '医生', 
    2 : '战士',
    3 : '吸血鬼',
    4 : '法师',
    5 : 'BOSS', 
    6 : '地神'
}

SH = {
    '普攻':0, 
    '火球':0, 
    '毒药':0, 
    '吸血':0, 
    '地震':0, 
    '震动':0
}

LVL = [0, 750, 1500, 2500, 3625,
    5100, 6650, 8600, 10800, 13000, 
    15675, 18300, 21450, 24850, 28125, 
    32000, 40375, 45000, 49875, 55500, 
    59325, 75350, 85675, 96000, 107500, 
    118950, 131625, 144200, 158050, 171750, 
    186775, 201600, 217800, 234600, 251125, 
    269100, 286750, 305900, 324675, 345000, 
    432550, 484050, 536425, 591800, 648000, 
    706100, 767275, 829200, 894250, 960000, 
    1346400, 1497600, 1653600, 1814400, 1980000, 
    13011600, 14760150, 16573500, 18456675, 20407500
]

BKGR = Back.GREEN
BKWT = Back.WHITE
BKRD = Back.RED
BKYL = Back.YELLOW
BKBL = Back.BLUE
BKMG = Back.MAGENTA
BKCY = Back.CYAN
BKBK = Back.BLACK

FRGR = Fore.GREEN
FRWT = Fore.WHITE
FRRD = Fore.RED
FRYL = Fore.YELLOW
FRBL = Fore.BLUE
FRMG = Fore.MAGENTA
FRCY = Fore.CYAN
FRBK = Fore.BLACK

DIM = Style.DIM
BRT = Style.BRIGHT
RST = Style.RESET_ALL


def speed_random(seed):
    s = seed
    s += 0x32efda
    s %= 0xcc510
    s += 0x75032b
    s %= 0x459ed
    return s

def randint(low, high):
    global rseed
    seed = speed_random(rseed)
    rseed += 1
    seed %= high - low + 1
    seed += low
    return seed


class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        if job == 1:
            self.hp = randint(2100, 2500)
            self.atk = randint(80, 90)
            self.skills = [5, 6, 10]
        elif job == 2:
            self.hp = randint(1200, 1300)
            self.atk = randint(120, 140)
            self.skills = [1, 4]
        elif job == 3:
            self.hp = randint(1200, 1300)
            self.atk = randint(170, 180)
            self.skills = [7, 9]
        elif job == 4:
            self.hp = randint(1200, 1300)
            self.atk = randint(80, 90)
            self.skills = [2, 3]
        elif job == 5:
            self.hp = randint(10000, 10000)
            self.atk = randint(190, 220)
            self.skills = [1, 8]
        elif job == 6:
            self.hp = randint(1400, 1700)
            self.atk = randint(110, 130)
            self.skills = [6, 8]
        else:
            self.atk = self.dfs = self.hp = self.ptp = 1
            self.skills = []
        
        kk = 3 if job != 5 else 5
        self.sy = ['', '', '']
        while kk > 0:
            kk -= 1
            hx = randint(1, len(SKLPMP))
            while hx in self.skills:
                hx = randint(1, len(SKLPMP))
            self.skills.append(hx)
        self.skills = sorted(self.skills)
        
        self.full = self.hp
        self.lvl = 1
        self.state = []
        self.points = 18
        self.score = 0
        self.lscore = 0
        self.cnt = 0
        self.d = False
    
    def _color_hp(self):
        full = f'/{self.full}'
        if self.hp >= (160 / 100) * self.full:
            return BKGR + FRBL + str(self.hp) + full
        elif self.hp >= (125 / 100) * self.full:
            return BKGR + FRBK + str(self.hp) + full
        elif self.hp >= (100 / 100) * self.full:
            return BKBL + FRBK + BRT + str(self.hp) + full
        elif self.hp >= (80 / 100) * self.full:
            return BKCY + FRWT + BRT + str(self.hp) + full
        elif self.hp >= (65 / 100) * self.full:
            return BKYL + FRWT + BRT + str(self.hp) + full
        elif self.hp >= (40 / 100) * self.full:
            return BKYL + FRRD + DIM + str(self.hp) + full
        elif self.hp >= (15 / 100) * self.full:
            return BKRD + FRWT + BRT + str(self.hp) + full
        elif self.hp > (0 / 100) * self.full:
            return BKRD + FRYL + str(self.hp) + full
        elif self.hp == (0 / 100) * self.full:
            return BKRD + FRYL + BRT + str(self.hp) + full
        else:
            return BKMG + FRWT + '???'
            
    def __str__(self):
        if self.d:
            color1 = FRRD
        else:
            color1 = ''
        
        a = f'{self.name}（{JOBPMP[self.job]}）:\n攻击次数 {self.cnt} 攻 {self.atk}  剩余血量 ' + RST + \
            self._color_hp() + RST + color1 + f'  技能点数 {self.points}  经验 {self.score} 等级 {self.lvl} 下一级所需经验 {LVL[self.lvl]}\n'
        b = '状态：'
        for i in STTPMP.keys():
            if self.state.count(i) > 0:
                b += STTPMP[i] + str(self.state.count(i)) + ' '
        b += '\n' if self.state != [] else ('正常\n' if not self.d else '死亡\n')
        if self.d:
            b += '死因：'
            for i in self.sy:
                b += i + ' '
            b += '\n'
        b += '技能：'
        for i in self.skills:
            b += str(i) + ':' + SKLPMP[i] + ' ' + str(SKLCD[self.job][i]) + '   '
        return color1 + a + b + '\n' + RST
    
    def attack(self, dp, flag=0):
        if not flag:
            self.cnt += 1
        if 2 in self.state:
            return ''
        atkdict = [0.64, 0.276, 0.229, 0.244, 0.313, 0.227, 0.405, 0.276, 0.229, 0.244, 1.253]
        attk = ceil(self.atk * atkdict[flag])
        attk = max(0, attk - (self.state.count(5) * 20) + (self.state.count(4) * 20))
        dp.hp -= attk
        dp.sy.append('普攻')
        self.score += attk
        SH['普攻'] += attk
        return f'{self.name} 发起攻击，{dp.name} 受到 {attk} 点伤害。\n'
    
    def del_state(self, flag=False):
        if len(self.state) != 0:
            p = randint(0, len(self.state) - 1)
            if self.state[p] in [1,2,3] or flag:
                x = self.state[p]
                del self.state[p]
                if x == 1:
                    return f'{self.name} 的' + STTPMP[x] + '症状减轻了一些\n'
                elif x == 2 or x == 6:
                    return f'{self.name} 的' + STTPMP[x] + '效果减弱了一些\n'
                elif x == 3:
                    return f'{self.name} 所在的区域' + STTPMP[x] + '减弱了一些\n'
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    
    def check(self):
        ret = ''
        if 1 in self.state and self.hp > 0:
            attk = randint(55, 70) * self.state.count(1)
            self.hp -= attk
            ret += f'{self.name} 中毒了，受到伤害 {attk} 点。\n'
            self.sy.append('中毒')
            SH['毒药'] += attk
        if 3 in self.state and self.hp > 0:
            attk = randint(5, 8) * self.state.count(3)
            self.hp -= attk
            ret += f'{self.name} 感受到了震动，受到伤害 {attk} 点。\n'
            self.sy.append('震动')
            SH['震动'] += attk
        if 6 in self.state and self.hp > 0:
            detk = randint(11, 23) * self.state.count(6)
            self.hp += detk
            ret += f'{self.name} 回血 {detk} 点\n'
        if (randint(1, 5) <= 2) and self.hp > 0:
            ret += self.del_state(flag=True)
        if self.hp <= 0 and not self.d:
            self.hp = 0
            ret += f'{self.name} 倒下了\n'
            self.points = 0
            self.d = True
            self.state = []
        if self.hp > 0:
            if self.score > self.lscore:
                ret += f'{self.name} 获得了 {self.score - self.lscore} 点经验！\n'
                self.lscore = self.score
            while LVL[self.lvl] <= self.score:
                self.lvl += 1
                ret += f'{self.name} 提升了等级！{self.name} 目前的等级为 {self.lvl}！\n'
            self.points += ceil(self.lvl / 5)
            self.sy = self.sy[-3:]
        return ret
    
    def add_state(self, stt):
        x = randint(2, 4)
        for i in range(x):
            self.state.append(stt)
        if stt == 1:
            return f'{self.name} ' + STTPMP[stt] + '了\n'
        elif stt == 2:
            return f'{self.name} 被' + STTPMP[stt] + '了\n'
        elif stt == 3:
            if randint(1, 10) == 7:
                x = randint(1, 3)
                for i in range(x):
                    self.state.append(stt)
                return f'{self.name} 遇到了非常强的' + STTPMP[stt] + '\n'
            else:
                return f'{self.name} 被' + STTPMP[stt] + '地带包围了\n'
        elif stt == 6:
            return f'{self.name} 获得' + STTPMP[stt] + '效果\n'
        return ''
    
    def skill(self, dp, skill):
        self.cnt += 1
        if (skill not in self.skills) or (self.points < SKLCD[self.job][skill]) or (2 in self.state):
            return ''
        self.points -= SKLCD[self.job][skill]
        ret = f'{self.name} 使用' + SKLPMP[skill] + '\n'
        if skill == 1:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            attk = ceil(self.atk * 1.285)
            dp.hp -= attk
            self.score += 360 + attk
            ret += f'{dp.name} 受到 {attk} 点伤害。\n'
            dp.sy.append('火球')
            SH['火球'] += attk
            self.points += 2
        elif skill == 2:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            ret += dp.add_state(2)
            self.score += 800
            self.points += 3
        elif skill == 3:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            ret += dp.add_state(1)
            self.score += 840
            self.points += 3
        elif skill == 4:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            natk = randint(5, 10)
            for i in range(natk):
                ret += self.attack(dp, flag=i + 1)
            self.points += 3
            self.score += 580
        elif skill == 5:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            detk = ceil(self.full * 0.127 + 132)
            dp.hp += detk
            ret += f'{dp.name} 回血 {detk} 点\n'
            ndtk = randint(2, 5)
            for i in range(ndtk):
                ret += dp.del_state()
            self.points += 3
            ret += dp.add_state(6)
            plusatk = ceil(self.atk * 0.39)
            dp.atk += plusatk
            self.score += 1040 + detk
            ret += f'{dp.name} 增加了 {plusatk} 点攻击力\n'
        elif skill == 6:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            detk2 = ceil(self.atk * 0.315)
            dp.atk += detk2
            ret += f'{dp.name} 提升攻击力 {detk2} 点。\n'
            self.score += 620 + (detk2) * 2
            self.points += 3
        elif skill == 7:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            attk = ceil(self.atk * 0.233)
            dp.hp -= attk
            datk = ceil(dp.atk * 0.056)
            dp.atk -= datk
            self.hp += attk
            self.score += 340 + attk
            ret += f'{dp.name} 受到 {attk} 点伤害，降低了 {datk} 点攻击力\n{self.name} 回血 {attk} 点\n'
            SH['吸血'] += attk
            dp.sy.append('吸血')
            self.points += 1
        elif skill == 8:
            attk = ceil(self.atk * 2.81)
            dpts = []
            for i in range(25):
                dpts.append(dp[randint(0, len(dp) - 1)])
            for i in dpts:
                if lst[int(i) - 1].d:
                    ret += str(lst[int(i) - 1].name) + ' 已经死亡。\n'
                    continue
                k = randint(0, 20)
                itk = attk // 25 + k
                lst[int(i) - 1].hp -= itk
                ret += str(lst[int(i) - 1].name) + '受到' + str(itk) + '点伤害。\n'
                lst[int(i) - 1].sy.append('地震')
                SH['地震'] += attk // len(dp) + k
                if randint(1, 10) == 8:
                    ret += lst[int(i) - 1].add_state(3)
            self.score += 1140 + attk
            self.points += 3
        elif skill == 9:
            if dp.d:
                ret += f'{dp.name} 已经死亡。\n'
                return ret
            attk = ceil(self.atk * 0.524)
            dp.hp -= attk
            datk = ceil(dp.atk * 0.126)
            dp.atk -= datk
            self.hp += attk
            self.score += 860 + attk
            ret += f'{dp.name} 受到 {attk} 点伤害，降低了 {datk} 点攻击力\n{self.name} 回血 {attk} 点\n'
            SH['吸血'] += attk
            dp.sy.append('吸血')
            self.points += 4
        elif skill == 10:
            detk = ceil(self.full * 0.135) + 170
            for i in dp:
                if lst[int(i) - 1].d:
                    ret += str(lst[int(i) - 1].name) + ' 已经死亡。\n'
                    continue
                k = randint(1, 6)
                itk = detk // len(dp) + k
                lst[int(i) - 1].hp += itk
                ret += f'{lst[int(i) - 1].name} 回血 {itk} 点\n'
                plusatk = ceil(self.atk * 0.195)
                lst[int(i) - 1].atk += plusatk
                ret += f'{lst[int(i) - 1].name} 增加了 {plusatk} 点攻击力\n'
                ret += lst[int(i) - 1].add_state(6)
            self.score += 1580 + detk
            self.points += 3
        return ret



os.system('cls')
print(RST)
print(f'欢迎您来到 {BKBL}F{BKMG}f{BKBL}I{BKMG}i{BKBL}G{BKMG}g{BKBL}H{BKMG}h{BKBL}T{BKMG}t{RST}')
print('''    ___    ___     ___    _  _    _____  
   | __|  |_ _|   / __|  | || |  |_   _| 
   | _|    | |   | (_ |  | __ |    | |   
  _|_|_   |___|   \___|  |_||_|   _|_|_  
_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
     __     _      __ _   _        _     
    / _|   (_)    / _` | | |_     | |_   
   |  _|   | |    \__, | | ' \    |  _|  
  _|_|_   _|_|_   |___/  |_||_|   _\__|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-\'"`-0-0-'"`-0-0-'"`-0-0-'

游戏目标：
将敌人全部打4，可以使用普攻，也可以使用技能
使用技能需要花费技能点，每个技能所需技能点数不同
祝您游戏愉快！
''')
s = input('按下回车进入游戏（如果有种子，请在这里输入后回车）：')
rseed = random.randint(100000, 999999)
try:
    rseed = int(s)
except:
    pass
os.system('cls')
print(f'本次游戏种子：{rseed}')
lst = [
    Player('吸吸鬼1', 3),
    Player('勇敢战士2', 2),  
    Player('土地之神3', 6),
    Player('奋斗战士4', 2), 
    Player('魔术师5', 4),
    Player('大医生6', 1),
    Player('护士7', 1),
    Player('魔法师8', 4)
]
print('伤害来源统计：')
for i in SH:
    print(i, SH[i])
print('-' * 120)
for i in lst:
    print(i)
now = 0
flag = False
while [i.hp for i in lst].count(0) < len(lst) - 1:
    flag = False
    try:
        now %= len(lst)
        while lst[now].d or 2 in lst[now].state:
            lst[now].cnt += 1 if 2 in lst[now].state else 0
            now += 1
            now %= len(lst)
        print(f'轮到 {lst[now].name} 了')
        cmd = input()
        if cmd == 'atk':
            ags = input()
            ls = ags.split(' ')
            os.system('cls')
            print(lst[now].attack(lst[int(ls[0]) - 1]))
            now += 1
        elif cmd == 'skl':
            ags = input()
            ls = ags.split(' ')
            os.system('cls')
            if ls[0][0] != '[':
                print(lst[now].skill(lst[int(ls[0]) - 1], int(ls[1])))
            else:
                print(lst[now].skill(eval(ls[0].strip('[').strip(']')), int(ls[1])))
            now += 1
        elif cmd == 'addpt':
            ag = input()
            os.system('cls')
            for i in lst:
                i.points += int(ag)
        elif cmd == 'pass':
            lst[now].cnt += 1
            now += 1
            os.system('cls')
        elif cmd == 'atkall':
            ag = int(input())
            for i in lst:
                if not i.d:
                    i.sy = ['', '', '被系统清除']
                    i.hp -= ag
            os.system('cls')
        elif cmd == 'edhp':
            ags = input()
            ls = ags.split(' ')
            lst[int(ls[0]) - 1].hp = int(ls[1])
            os.system('cls')
        elif cmd == 'exit':
            break
        else:
            os.system('cls')
            raise RuntimeError
    except Exception as e:
        os.system('cls')
        print(f'错误 {e}')
    else:
        flag = True
    print('伤害来源统计：')
    for i in SH:
        print(i, SH[i])
    print()
    if flag:
        for i in lst:
            print(i.check(), end='')
    print('-' * 60)
    for i in lst:
        print(i)
print(RST)
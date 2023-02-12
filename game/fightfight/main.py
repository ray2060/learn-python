from math import ceil
import os
from colorama import init, Fore, Back, Style

STTPMP = {
    1 : '中毒', 
    2 : '冰冻',
    3 : '震动',
    4 : '大力',
    5 : '虚弱',
    6 : '回血'
}

SKLPMP = {
    1 : '火球术',
    2 : '冰冻术',
    3 : '施毒术',
    4 : '连击',
    5 : '治愈术',  
    6 : '铁壁', 
    7 : '吸血', 
    8 : '地震'
}

SKLCD = {
    1 : 23,
    2 : 35,
    3 : 37,
    4 : 31,
    5 : 42,  
    6 : 36, 
    7 : 45, 
    8 : 39
}
SH = {
    '普攻':0, 
    '火球':0, 
    '毒药':0, 
    '吸血':0, 
    '地震':0, 
    '震动':0
}


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


cnt = 13331
def speed_random(seed):
    s = seed
    s += 0x32efda
    s %= 0xcc510
    s += 0x75032b
    s %= 0x459ed
    return s

def randint(low, high):
    global cnt
    seed = speed_random(cnt)
    cnt += 1
    seed %= high - low + 1
    seed += low
    return seed


class Player:
    def __init__(self, name, mode):
        self.name = name
        if mode == 1:
            self.atk = randint(90, 120)
            self.dfs = randint(80, 110)
            self.hp = randint(1200, 1400)
        elif mode == 2:
            self.atk = randint(150, 180)
            self.dfs = randint(160, 190)
            self.hp = randint(300, 450)
        elif mode == 3:
            self.atk = randint(75, 85)
            self.dfs = randint(80, 95)
            self.hp = randint(280, 340)
        elif mode == 4:
            self.atk = randint(80, 95)
            self.dfs = randint(85, 105)
            self.hp = randint(300, 360)
        else:
            self.atk = randint(70, 90)
            self.dfs = randint(80, 100)
            self.hp = randint(290, 350)
            
        kk = randint(5 if mode in [1, 2] else 3, 7 if mode in [1, 2] else 6)
        self.skills = []
        while kk > 0:
            kk -= 1
            hx = randint(1, len(SKLPMP))
            while hx in self.skills:
                hx = randint(1, len(SKLPMP))
            self.skills.append(hx)
        self.skills = sorted(self.skills)
        
        self.full = self.hp
        self.state = []
        self.cd = 15
        self.score = 0
        self._cnt = 0
        self.d = False
    
    def _color_hp(self):
        if self.hp >= (200 / 100) * self.full:
            return BKGR + FRBL + str(self.hp)
        elif self.hp >= (140 / 100) * self.full:
            return BKGR + FRBK + str(self.hp)
        elif self.hp >= (100 / 100) * self.full:
            return BKBL + FRBK + BRT + str(self.hp)
        elif self.hp >= (80 / 100) * self.full:
            return BKCY + FRWT + BRT + str(self.hp)
        elif self.hp >= (65 / 100) * self.full:
            return BKYL + FRWT + BRT + str(self.hp)
        elif self.hp >= (40 / 100) * self.full:
            return BKYL + FRRD + DIM + str(self.hp)
        elif self.hp >= (15 / 100) * self.full:
            return BKRD + FRWT + BRT + str(self.hp)
        elif self.hp > (0 / 100) * self.full:
            return BKRD + FRYL + str(self.hp)
        elif self.hp == (0 / 100) * self.full:
            return BKRD + FRYL + BRT + str(self.hp)
        else:
            return BKMG + FRWT + '???'
            
    def __str__(self):
        if self.d:
            color1 = FRRD
        else:
            color1 = ''
        
        a = f'{self.name}:\n攻击次数 {self._cnt} 攻 {self.atk}  防 {self.dfs}  剩余血量 ' + RST + \
            self._color_hp() + RST + color1 + f'  技能点数 {self.cd}  分数 {self.score}\n'
        b = '状态：'
        for i in STTPMP.keys():
            if self.state.count(i) > 0:
                b += STTPMP[i] + str(self.state.count(i)) + ' '
        b += '\n' if self.state != [] else ('正常\n' if not self.d else '死亡\n')
        b += '技能：'
        for i in self.skills:
            b += str(i) + ':' + SKLPMP[i] + ' ' + str(SKLCD[i]) + '   '
        return color1 + a + b + '\n' + RST
    
    def lose_hp(self, dt):
        return min(ceil(1.1 * dt), max(ceil(0.68 * dt), (ceil((dt / self.dfs) - 1) * 2 + 1) * dt))
    
    def attack(self, dfs_ply, flag=False):
        if not flag:
            self._cnt += 1
        if 2 in self.state:
            return ''
        attk = randint(ceil(self.atk * (0.3 if flag else 0.7)), ceil(self.atk * (0.55 if flag else 1.3)))
        attk = max(0, attk - (self.state.count(5) * 20) + (self.state.count(4) * 20))
        attk = dfs_ply.lose_hp(attk)
        dfs_ply.hp -= attk
        self.score += attk + (dfs_ply.score // 3)
        SH['普攻'] += attk
        return f'{self.name} 发起攻击，{dfs_ply.name} 受到 {attk} 点伤害。\n'
    
    def del_state(self, flag=False):
        if len(self.state) != 0:
            p = randint(0, len(self.state) - 1)
            if self.state[p] in [1,2,3,5] or flag:
                x = self.state[p]
                del self.state[p]
                if x == 1 or x == 5:
                    return f'{self.name} 的' + STTPMP[x] + '症状减轻了一些\n'
                elif x == 2 or x == 4 or x == 6:
                    return f'{self.name} 的' + STTPMP[x] + '效果减弱了一些\n'
                elif x == 3:
                    return f'{self.name} 所在的区域' + STTPMP[x] + '减弱了一些\n'
            else:
                return ''
        else:
            return ''
    
    def check(self):
        ret = ''
        if 1 in self.state and self.hp > 0:
            attk = randint(10, 25) * self.state.count(1)
            self.hp -= attk
            ret += f'{self.name} 中毒了，受到伤害 {attk} 点。\n'
            SH['毒药'] += attk
        if 3 in self.state and self.hp > 0:
            attk = randint(7, 15) * self.state.count(3)
            self.hp -= attk
            ret += f'{self.name} 感受到了震动，受到伤害 {attk} 点。\n'
            SH['震动'] += attk
        if 6 in self.state and self.hp > 0:
            detk = randint(30, 80)
            self.hp += detk
            ret += f'{self.name} 回血 {detk} 点\n'
        if (randint(1, 5) <= 2) and self.hp > 0:
            ret += self.del_state(flag=True)
        if self.hp <= 0 and not self.d:
            self.hp = 0
            ret += f'{self.name} 倒下了\n'
            self.cd = 0
            self.d = True
            self.state = []
        if self.hp > 0:
            self.cd += randint(1 + (self.score // 350), 2 + (self.score // 340))
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
            if randint(1, 4) == 2:
                x = randint(2, 4)
                for i in range(x):
                    self.state.append(stt)
                return f'{self.name} 遇到了非常强的' + STTPMP[stt] + '\n'
            else:
                return f'{self.name} 被' + STTPMP[stt] + '地带包围了\n'
        elif stt == 4:
            return f'{self.name} 觉得自己变成了' + STTPMP[stt] + '神\n'
        elif stt == 5:
            return f'{self.name} 觉得自己变得' + STTPMP[stt] + '了\n'
        elif stt == 6:
            return f'{self.name} 获得' + STTPMP[stt] + '效果\n'
        return ''
    
    def us_skill(self, dfs_ply, skill):
        self._cnt += 1
        if (skill not in self.skills) or (self.cd < SKLCD[skill]) or (2 in self.state):
            return ''
        self.cd -= SKLCD[skill]
        ret = f'{self.name} 使用' + SKLPMP[skill] + '\n'
        if skill == 1:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            attk = randint(max(0, self.atk + 20), self.atk + 60)
            attk = dfs_ply.lose_hp(attk)
            dfs_ply.hp -= attk
            self.score += attk + (dfs_ply.score // 3)
            ret += f'{dfs_ply.name} 受到 {attk} 点伤害。\n'
            SH['火球'] += attk
            self.cd += randint(2 + (self.score // 350), 4 + (self.score // 340))
        elif skill == 2:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            ret += dfs_ply.add_state(2)
            self.score += randint(150, 300)
            self.cd += randint(3 + (self.score // 350), 4 + (self.score // 340))
        elif skill == 3:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            ret += dfs_ply.add_state(1)
            self.score += randint(150, 300)
            self.cd += randint(3 + (self.score // 350), 4 + (self.score // 340))
        elif skill == 4:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            natk = randint(2, 6)
            for i in range(natk):
                ret += self.attack(dfs_ply, flag=True)
            self.cd += randint(4 + (self.score // 350), 7 + (self.score // 340))
        elif skill == 5:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            detk = randint(180, 300)
            dfs_ply.hp += detk
            self.score += detk + randint(detk // 3, detk // 2)
            ret += f'{dfs_ply.name} 回血 {detk} 点\n'
            ndtk = randint(2, 5)
            for i in range(ndtk):
                ret += dfs_ply.del_state()
            self.cd += randint(5 + (self.score // 200), 9 + (self.score // 180))
            ret += dfs_ply.add_state(6)
            ret += dfs_ply.add_state(4)
        elif skill == 6:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            detk1 = randint(ceil(dfs_ply.dfs * 0.15), ceil(dfs_ply.dfs * 0.35))
            detk2 = randint(ceil(dfs_ply.atk * 0.15), ceil(dfs_ply.atk * 0.35))
            dfs_ply.dfs += detk1
            dfs_ply.atk += detk2
            ret += f'{dfs_ply.name} 获得防御力 {detk1} 点，攻击力 {detk2} 点。\n'
            self.score += randint(detk1 + detk2 + 20, detk1 + detk2 + 40)
            self.cd += randint(4 + (self.score // 350), 5 + (self.score // 340))
        elif skill == 7:
            if dfs_ply.d:
                ret += f'{dfs_ply.name} 已经死亡。\n'
                return ret
            attk = randint(max(0, self.atk - 40), self.atk - 10)
            attk = dfs_ply.lose_hp(attk)
            dfs_ply.hp -= attk
            self.hp += attk
            self.score += randint(320, 400)
            ret += f'{dfs_ply.name} 受到 {attk} 点伤害\n{self.name} 回血 {attk} 点\n'
            SH['吸血'] += attk
            self.cd += randint(9 + (self.score // 750), 14 + (self.score // 720))
            ret += dfs_ply.add_state(5)
        elif skill == 8:
            attk = randint(ceil(self.atk * 1.5), self.atk * 2) + (len(dfs_ply) * 20)
            for i in dfs_ply:
                if lst[int(i) - 1].d:
                    ret += str(lst[int(i) - 1].name) + ' 已经死亡。\n'
                    continue
                k = randint(1, 6)
                itk = lst[int(i) - 1].lose_hp(attk // len(dfs_ply) + k)
                lst[int(i) - 1].hp -= itk
                ret += str(lst[int(i) - 1].name) + '受到' + str(itk) + '点伤害。\n'
                SH['地震'] += attk // len(dfs_ply) + k
                ret += lst[int(i) - 1].add_state(3)
            self.score += randint(attk + 50, attk + 150)
            self.cd += randint(5 + (self.score // 350), 7 + (self.score // 340))
        return ret


lst = [
    Player('你', 1), 
    Player('猪队友', 2), 
    Player('敌人1', 3), 
    Player('敌人2', 4), 
    Player('敌人3', 5)
]
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
input('按下回车键进入游戏')
os.system('cls')
print('伤害来源统计：')
for i in SH:
    print(i, SH[i])
print('-' * 60)
for i in lst:
    print(i)
while [i.hp for i in lst].count(0) < len(lst) - 1:
    try:
        cmd = input()
        if cmd == 'atk':
            ags = input()
            ls = ags.split(' ')
            os.system('cls')
            print(lst[int(ls[0]) - 1].attack(lst[int(ls[1]) - 1]))
        elif cmd == 'skl':
            ags = input()
            ls = ags.split(' ')
            os.system('cls')
            if ls[1][0] != '[':
                print(lst[int(ls[0]) - 1].us_skill(lst[int(ls[1]) - 1], int(ls[2])))
            else:
                print(lst[int(ls[0]) - 1].us_skill(eval(ls[1].strip('[').strip(']')), int(ls[2])))
        elif cmd == 'adcd':
            ag = input()
            os.system('cls')
            for i in lst:
                i.cd += int(ag)
        elif cmd == 'exit':
            break
        else:
            os.system('cls')
    except:
        os.system('cls')
    print('伤害来源统计：')
    for i in SH:
        print(i, SH[i])
    print()
    for i in lst:
        print(i.check(), end='')
    print('-' * 60)
    for i in lst:
        print(i)
print(RST)
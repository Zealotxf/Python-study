from time import sleep
from progressbar import progress_bar
from ball import ball_bar
from random import randint

class Scene(object):
    def progress():
        progress_bar()
    pass

class NamekWild(Scene):
    def Scene_claim():
        print("在那美克星荒野，悟空一行人迎来了与弗利萨的最终决战。")

class NamekVillage(Scene):
    def Scene_claim():
        print("悟空一行人来到了那美克星村落，准备寻找龙珠的下落。然而弗利萨与他的手下也到来了")

class Fight(Scene):
    def Startfight():
        print("开始战斗！")

    def Hostile():
        print("首先登场的是基纽特种队。")

class Death(Scene):
    def Death():
        print("你的生命值为0，你输了。")

class Person(object):
    def __init__(self):
        self.blood = 1000
        self.capacity = 100
    def action(self):
        self.punch = 1 * self.capacity
        self.kick = 2 * self.capacity
        self.qigong = 3 * self.capacity

class Gokong(Person):
    def __init__(self):
        self.blood = 1500
        self.capacity = 250
    def skill(self):
        print("悟空变成超级赛亚人！")
        self.blood = 5000
        self.capacity = 500
    def TurtleQiGong(self):
        self.qigong = 5.0 * self.capacity

class Vegeta(Person):
    def __init__(self):
        self.blood = 1000
        self.capacity = 150
    def skill(self):
        print("贝吉塔使用了最终闪光！")
        self.qigong = 4.0 *self.capacity

class Klin(Person):
    def __init__(self):
        self.blood = 800
        self.capacity = 80
    def skill(self):
        print("克林使用了气元斩！")
        self.qigong = 200

class GoFan(Person):
    def __init__(self):
        self.blood = 800
        self.capacity = 90
    def skill(self):
        print("悟饭爆发出了愤怒的力量！")
        self.capacity = 150

class piccolo(Person):
    def skill(self):
        print("短笛治愈了自己！")
        self.blood += 100

class Frieza(Person):
    def __init__(self):
        self.blood = 1000
        self.capacity = 300
    def modelchange_1(self):
        print("弗利萨的身体变得巨大化。")
        self.blood = 2000
        self.capacity = 350
    def modelchange_2(self):
        print("弗利萨变化形态，和异型一般。")
        self.blood = 3000
        self.capacity = 400
    def modelchange_3(self):
        print("弗利萨变化成了最终形态！")
        self.blood = 4000
        self.capacity = 450

class GiNyu(Person):
    def __init__(self):
        self.blood = 800
        self.capacity = 200

def identity_init_(i):
        if team[i] == "悟空":
            team[i] = Gokong
        elif team[i] == "贝吉塔":
            team[i] = Vegeta
        elif team[i] == "克林":
            team[i] = Klin
        elif team[i] == "悟饭":
            team[i] = GoFan
        else:
            team[i] = piccolo

def fight_engineer_1():
    print(team[0],"VS 基纽")
    identity_init_(0)
    GiNyu.__init__(GiNyu)
    team[0].__init__(team[0])

    combat = ["0.出拳", "1.鞭腿", "2.气功波","3.技能"]
    action_choose= {"0": "出拳",
                    "1": "鞭腿",
                    "2": "气功波",
                    "3": "技能"}

    fightaction = Person
    Person.__init__(fightaction)

    i = 0
    while GiNyu.blood > 0:
        print("<======================================================================================>")
        print("基纽的生命值:", GiNyu.blood, "                      ", team_choose[i], "的生命值:", team[i].blood)
        print("基纽的战斗力:", GiNyu.capacity, "                      ", team_choose[i], "的战斗力:", team[i].capacity )
        print("选择你的攻击方式:")
        print(combat)
        x = input("==> ")
        action_ = action_choose[x]
        print("你选择了:", action_, "\n")
        team[i].action(fightaction)
        if action_ == 0:
            GiNyu.blood -= fightaction.punch
        elif action_ == 1:
            GiNyu.blood -= fightaction.kick
        else:
            GiNyu.blood -= fightaction.qigong

        y = randint(0, 9)
        if y >= 0 and y < 3:
            print("基纽使用了出拳\n")
            team[i].blood -= fightaction.punch
        elif y>= 3 and y < 6:
            print("基纽使用了鞭腿\n")
            team[i].blood -= fightaction.kick
        else:
            print("基纽使用了气功波\n")
            team[i].blood -= fightaction.qigong

        if team[i].blood <= 0 and GiNyu.blood > 0:
            print(team_choose[i], "战败！")
            print("\n")
            i += 1
            identity_init_(i)
            print(team_choose[i],"VS 基纽")
        else:
            pass
    print("基纽被打败，弗利萨大王上场！\n")
    fight_engineer_2(i)

def fight_engineer_2(i):
    print(team_choose[i],"VS 弗利萨")
    identity_init_(i)
    Frieza.__init__(Frieza)
    team[i].__init__(team[i])

    combat = ["0.出拳", "1.鞭腿", "2.气功波", "3.技能"]
    action_choose= {"0": "出拳",
                    "1": "鞭腿",
                    "2": "气功波",
                    "3": "技能"}

    fightaction = Person
    Person.__init__(fightaction)

    while Frieza.blood > 0:
        print("<=================================================>")
        print("弗利萨的生命值:", Frieza.blood, "                      ", team_choose[i], "的生命值:", team[i].blood)
        print("弗利萨的战斗力:", Frieza.capacity, "                      ", team_choose[i], "的战斗力:", team[i].capacity )
        print("选择你的攻击方式:")
        print(combat)
        x = input("==> ")
        action_ = action_choose[x]
        print("你选择了:", action_, "\n")
        team[i].action(fightaction)
        if action_ == 0:
            Frieza.blood -= fightaction.punch
        elif action_ == 1:
            Frieza.blood -= fightaction.kick
        else:
            Frieza.blood -= fightaction.qigong
        y = randint(0, 9)
        if y >= 0 and y < 3:
            print("弗利萨使用了出拳")
            team[i].blood -= fightaction.punch
        elif y>= 3 and y < 6:
            print("弗利萨使用了鞭腿")
            team[i].blood -= fightaction.kick
        else:
            print("弗利萨使用了气功波")
            team[i].blood -= fightaction.qigong

        if team[i].blood <= 0 and GiNyu.blood > 0:
            print(team_choose[i], "战败！")
            print("\n")
            i += 1
            identity_init_(i)
            print(team_choose[i],"VS 弗利萨")
        else:
            pass
    print("弗利萨被打败，你获得最终胜利！\n")

"""def progress_bar():
    bar = "■■"
    barren = ""
    for i in range(0,10):
        barren +=bar
        print(barren)
        sleep(1)
        if i == 9:
            print("加载完成。")
        else:
            pass"""

print("""为了使用那美克星的大龙珠悟空一行人来到了那美克星。为了争夺龙珠他们将与弗利萨作战。
输入数字来选择出战人物。
你可以选择三个人物。""")
print("""0. 悟空
1. 贝吉塔
2. 克林
3. 悟饭
4. 短笛""")

people_choose = { "0": "悟空",
                  "1": "贝吉塔",
                  "2": "克林",
                  "3": "悟饭",
                  "4": "短笛"}
team = [" ", " ", " "]
select=[" ", " ", " ", " "]
for i in range(0,3):
    select[i] = input("==> ")
    if  select[i] == select[i-1] or select[i] == select[i+1]:
        print("选择失败，人物重复，请重新选择")
    else:
         team[i] = people_choose[select[i]]
         print("选择成功！")

team_choose = {0: team[0],
               1: team[1],
               2: team[2]}
print("你选择的人物是:", end = " ")
print(team)


Namek_village = NamekVillage
Namek_village.progress()
Namek_village.Scene_claim()

village_fight = Fight
village_fight.Startfight()
village_fight.Hostile()

fight_engineer_1()

Namek_wild = NamekWild
Namek_wild.progress()
Namek_wild.Scene_claim()

wild_fight = Fight
wild_fight.Startfight()
wild_fight.Hostile()

fight_engineer_1()
ball_bar()

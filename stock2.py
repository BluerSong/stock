import time
import random
ed = 0
e = 0
muda2 = 0
plus = None
ci = 0#工具变量
ci2 = int(input("公司数(1~14)>>>"))#公司总数（用于def company）
dd = []#空列表
dd2 = []#同dd
dic2 = []#公司名筛选用
invested = []#投资数
factor = []#配合coefficient
hard = int(input("难度(1~3,小到大)>>>"))#资金
if hard == 1:
    capital = random.randint(20000,100000)
elif hard == 2:
    capital = random.randint(10000, 20000)
elif hard == 3:
    capital = random.randint(5000,10000)
elif hard == 4:
    print('恭喜你触发彩蛋"自定义模式"，请输入初始资金')
    capital = int(input(">>>"))
muda = capital
end = int(input("目标是(资金数)>>>"))
instate = False
coefficient = 0#资金加减系数

def dict():
    global ci2,dic2
    i = 1
    while(i<ci2+1):
        c = random.randint(1,ci2)
        if c not in dic2:
            dic2.append(c)
            i += 1
    return dic2
def pom(plus):#随机加减
    a = random.randint(1,100)
    if invested == True:
        if a+plus>50:
            return 1
        else:
            return 0
    else:
        if a>50:
            return 1
        else:
            return 0


def campany():
    global ci,ci2
    while (ci < ci2):  # 市值添加进列表（dd）
        dd.append(random.randint(1, 100))
        dd2.append(ci+1)
        ci += 1
    return dd,dd2
campany()
dict()
def printf():#market配套
    a = 1
    global dd,dd2,ci2,dic
    while(a-1<ci2):
        print(dd2[a-1],dic[str(dic2[a-1])],dd[a-1],"/股")
        a +=1
        time.sleep(0.1)
def randomh():#实现股市日期更替涨与跌（以百分数表示）
    global ci2,dd2,dd,instate,invested,choose,capital,coefficient,e
    a = 1
    e = 0
    o = 0
    while(a-1<ci2):
        if dd[a-1]<=0:
            while o<1:
                u = random.randint(1, 14)
                if u not in dic2:
                    dic2[a-1] = u
                    o += 1
            dd[a-1] = random.randint(1,100)
        if instate == False:#投资状态为假
            pom(plus)
            if pom(plus) == 1:
                b = random.randint(1,4)
                coefficient = b/dd[a-1]
                factor.append(1+coefficient)
                dd[a - 1] = dd[a - 1] + b
                print(dic[str(dic2[a-1])],dd[a-1],"+%"+str(coefficient*100))
            else:
                b = random.randint(1,4)
                coefficient = b/dd[a-1]
                factor.append(1-coefficient)
                dd[a - 1] = dd[a - 1] - b
                print(dic[str(dic2[a-1])],dd[a-1],"-%"+str(coefficient*100))
            a += 1
        else:#投资状态为真
            f = pom(invested[e]//100)
            if f == 1:
                b = random.randint(1,4)
                coefficient = b / dd[a-1]
                factor.append(1+coefficient)
                dd[a-1] = dd[a-1] + b
                print(dic[str(dic2[a-1])],dd[a-1],"+%" + str((coefficient*100)))
                e += 1
            else:
                b = random.randint(1,4)
                coefficient = b / dd[a-1]
                factor.append(1-coefficient)
                dd[a-1] = dd[a-1] - b
                print(dic[str(dic2[a-1])],dd[a-1],"-%" + str((coefficient*100)))
                e += 1
            a += 1
    instate = False
while ed<ci2:
    invested.append(0)
    ed +=1

dic={#暂时没有用的字典
    "1":"Amazon",
    "2": "Facebook",
    "3":"Alphabet",
    "4":"Satorp",
    "5":"Shell",
    "6":"Walmart",
    "7":"Zip2",
    "8":"Space X",
    "9":"X.com",
    "10":"HyperGryph",
    "11":"The Boring Company",
    "12":"Solar City",
    "13":"Steam",
    "14":"BP",
}
while True:#操作界面
    if muda2 == 0:
        if capital > end:
            print("你赢了，是否结束?")
            print("1,结束 2,继续(自由模式)")
            end2 = input(">>>")
            if end2 == 1:
                break
            muda2 = 1
    print("目前可用资金",str(capital))
    if capital < 0:
        print("你破产了，游戏结束")
        break
    answer = input(">>>")
    if answer == "market":
        printf()
    elif answer == "help":
        print("游戏规则为:")
        print("1指令部分 2解释游戏内关键字")
        ans = int(input(">>>"))
        if ans == 1:
            print("market:上市公司价格一览(随时间变化)")
            print("pass:结束当前一轮操作，随后显示股市涨跌情况")
            print("invest:投资(以手(一百股)为单位)")
            print("invested:当前一轮的股市价格乘股份(已投资资金)")
            print("sale:抛售(售卖当前拥有股份(以股为单位))")
            print("capital:计算所有资金")
            print("exit:退出游戏")
        else:
            print("目前可用资金:全部资金-已投资资金")
            print("全部资金:目前可用资金+已投资资金，已投资资金随股价涨跌而变动")
            print("在难度选择中选4有惊喜")
    elif answer == "pass":
        randomh()
    elif answer == "invest":
        instate = True
        i = 0
        while i < ci2:
            print(dic[str(dic2[i])], end="")
            try:#规避错误(空数据)
                a = int(input("数目(手(100股)为单位)>>>"))
                a=a*100
            except:
                a = 0
                invested[i] += a
                i += 1
            else:
                invested[i] += a
                capital -= a * dd[i]
                i += 1
    elif answer == "invested":
        i = 0
        while i<ci2:
            print(invested[i]*dd[i])
            i += 1
    elif answer == "sale":
        i = 0
        while i < ci2:
            print(dic[str(dic2[i])], end="")
            try:  # 规避错误(空数据)
                print(dic[str(dic2[i])],"持有股份",invested[i],end="")
                a = input("数目>>>")
                if a != "all":
                    a = int(a)
            except:
                a = 0
                i += 1
            else:
                if a == "all":
                    capital += invested[i] * dd[i]
                    invested[i] -= invested[i]
                    i += 1
                elif a<0 or a>invested[i]*100:
                    print("数目错误")
                    i += 1
                else:
                    invested[i] -= a
                    capital += a * dd[i]
                    i += 1
    elif answer == "capital":
        i = 0
        v = 0
        while i < ci2:
            v += invested[i] * dd[i]
            i += 1
        print("全部资金",v+capital,"初始资金",muda)
    elif answer == "exit":
        print("游戏结束")
        break

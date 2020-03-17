import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


class Circle:
    def __init__(self,x,y,r):
            self.x = x
            self.y = y
            self.radius = abs(r)
    def Center(self):#圆心坐标
        center = complex(self.x,self.y)
        return center
    def Print(self):
        '''
        输出圆的信息
        '''
        x = self.x
        y = self.y
        r = self.radius
        a = "圆心坐标："+str(x)+' '+str(y)+" 半径："+str(r)
        print(a)
        return a
    # 判断该圆是否处于限定范围内

    def InRange(self):
        x = self.x
        y = self.y
        r = self.radius
        l = abs(x - r)
        m = abs(x + r)
        u = abs(y + r)
        d = abs(y - r)
        if max(l,m,u,d) > 1:
            return False
        else:
            return True
        
    def Distance(self,cire):
            '''
            判断两个圆之间的距离
            '''
            c1 = abs(self.Center() - cire.Center())
            c2 = self.radius + cire.radius
            c = c1-c2
            return c


    def OverLap(self,cire):
        '''
        判断两个圆是否相交
        '''
        c = self.Distance(cire)
        if c<0:
            return True
        else:
            return False
    # 将此对象添加到列表c_list中,返回是否添加成功

    # 需要判断该对象是否符合条件：和其他的圆无重叠部分

    def Inside(self,cire):
        '''
        判断新生成的圆是否在其他圆内
        '''
        r1 = cire.radius
        c1 = cire.Center()
        d = abs(self.Center()-c1)
        dr = abs(self.radius - r1)
        if d<=dr:
            return True
        else:
            return False
    
    def Append(self,c_list):
        '''
        加入列表中
        '''
        if self.InRange():
            i = True
            if len(c_list) == 0:
                c_list.append(self)
                return True
            else:
                for c in c_list:
                    i = not self.Inside(c) and not self.OverLap(c)
                    
                if i:
                    c_list.append(self)
                    return True
                else:
                    return False
    
        else:
            return False
# 计算最大可行半径
def Max_Radius(cir,c_list):
    '''最大可行半径'''
    x = cir.x
    y = cir.y
    r = cir.radius
    R_list = [1-x,1+x,1-y,1+y]
    if not len(c_list) == 0:
        for c in c_list:
            r = c.Distance(cir)
            R_list.append(r)
            
    return min(R_list)

def Print_Circle(c_list):
    for c in c_list:
        c.Print()
# 使用matplotlib进行绘图
def Plot(c_list):
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    theta = np.linspace(0, 2 * np.pi, 90)
    for c in c_list:
        x = c.x
        y = c.y
        r = c.radius
        plt.plot(x + r * np.cos(theta), y + r * np.sin(theta), 'r')
    plt.show()

# 计算在给定圆的数量的情况下，r^2最大时对应的圆的列表。方法二

def Optimize(c_num):
    c_list = []
    # 向列表中添加新圆，直到总数符合要求
    while len(c_list) < c_num:
        
        if len(c_list) == 0:
            c = Circle(0,0, 1)
            c.Append(c_list)
        else:
            re = (len(c_list)) % 4
            # 在四个象限中轮流初始化
            if re == 0:
                x = random.uniform(0, 1)
                y = random.uniform(0, 1)
            elif re == 1:
                x = random.uniform(-1, 0)
                y = random.uniform(0, 1)
            elif re == 2:
                x = random.uniform(-1, 0)
                y = random.uniform(-1, 0)
            elif re == 3:
                x = random.uniform(0, 1)
                y = random.uniform(-1, 0)
            c = Circle(x, y, 0)            # 使用优化器，计算局部最优解
            x0 = minimize(fun(c_list), (c.x, c.y),
                                  method='SLSQP')
            # 将新圆更新为局部最优解，并添加进列表
            c.x = float(x0.x[0])
            c.y = float(x0.x[1])
            c.radius = Max_Radius(c, c_list)
            c.Append(c_list)
#    for c in c_list:
#        c.Print()
#        print("***********")
    return c_list

# 优化器，目标为使最大可能半径尽可能大
def fun(c_list):
    a = lambda x: 1 - Max_Radius(Circle(x[0], x[1], 0), c_list)
    return a
#最终要求的解
def Sum(c_list):
    s = 0
    for c in c_list:
        s += c.radius**2
    return s

if __name__ == "__main__":
    circle_num = 2
    # c_list = Random_Max_R_Square(circle_num)
    c_list = Optimize(circle_num)
    R2 = Sum(c_list)
    print("sum r^2的最大值为\t", R2)
    print("对应圆的参数")
    Print_Circle(c_list)
    Plot(c_list)
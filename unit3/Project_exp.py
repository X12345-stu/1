import random
import numpy as np
import matplotlib as plt
'''
随机生成圆，并且求出它到边界的最大半径，如果满足不重叠的要求就加入圆形列表中。
'''
class Circle:
 
    #定义构造函数
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
        print("圆心坐标："+x+' '+y+"\n半径： "+r)
        
    def InRange(self):
        '''
        判断是否超出范围[-1,1]
        '''
        x = self.x
        y = self.y
        r = self.radius
        l = abs(x-r)
        r = abs(x+r)
        u = abs(y+r)
        d = abs(y-r)
        a = max(l,r,u,d)
        if a>1:
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
        
    def Overlap(self,cire):
        '''
        判断两个圆是否相交
        '''
        c = self.Distance(cire)
        if c<0:
            return True
        else:
            return False
    
    def Inside(self,cire):
        '''
        判断新生成的圆是否在其他圆内
        '''
        r1 = cire.radius
        c1 = cire.Center()
        d = abs(self.Center()-c1)
        if d<=r1 or d<=self.radius:
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
                    i = not self.Inside(c) and not self.Overlap(c)
                    
                if i:
                    c_list.append(self)
                    return True
                else:
                    return False
    
        else:
            return False
    
def Max_radius(cir,c_list):
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

def Sum(c_list):
    s = 0
    for c in c_list:
        s += c.radius**2
    return s 

def Print_circle(c_list):
    for c in c_list:
        c.Print()
    
def Plot_Circle(c_list):
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

def Random_max(c_n):
    c_list = []
    while len(c_list) <= c_n:
        if len(c_list) == 0:
            x = 0
            y = 0
            r = 1
        else:
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            r = 0
            
        cir = Circle(x,y,r)
        cir.radius = Max_radius(cir,c_list)
        cir.Append(c_list)
    return c_list
     
            
    
circle_number = 5
c_list = Random_max(circle_number)
SUM = Sum(c_list)
print("最大半径平方和为："+SUM)
Plot_circle(c_list) 
Print_circle(c_list)
        
    
    
        
    
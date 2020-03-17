import io
import sys
import unittest
from Project_exp import Circle#用于测试类
from Project_exp import Max_Radius,Optimize,Sum#测试最大的半径,


#def stub_stdout(testcase_inst):
#
#    stdout = sys.stdout
#
#    def cleanup():
#
#        sys.stdout = stdout
#
#    testcase_inst.addCleanup(cleanup)
#
#    sys.stdout = io.StringIO()
    
class CircleTestCase(unittest.TestCase):
    def setUp(self):
       self.c1 = Circle(0,0.5,0.5)
       self.c2 = Circle(0.5,0.5,3)
       self.c3 = Circle(-0.5,0,0.1)
       self.c4 = Circle(0,0,0.5)
    def test_Center(self):
        ans = self.c2.Center()
        self.assertEqual(ans,(0.5+0.5j))#返回坐标
    
    def test_Print(self):
          ans = self.c2.Print()
          self.assertEqual(ans,'圆心坐标：0.5 0.5 半径：3')#unit test输出流还没有完全学会
#          stub_stdout(self)
#          self.c2.Print()
#          self.assertEqual(str(sys.stdout.getvalue()), '7\n')
            
    def test_Inrange(self):
        ans = self.c1.InRange()#在范围内
        ans1 =  self.c2.InRange()#半径为3，不在范围内
        self.assertTrue(ans)
        self.assertFalse(ans1)
        
    def test_Distance(self):
        ans = self.c1.Distance(self.c2)#计算两个圆的边界的距离
        self.assertEqual(ans,-3)
    
    def test_OverLap(self):
        ans = self.c1.OverLap(self.c2)#有交点
        self.assertTrue(ans)
        ans = self.c1.OverLap(self.c3)#无交点
        self.assertFalse(ans)
    
    def test_Inside(self):
        ans = self.c1.Inside(self.c2)#c2半径很大
        self.assertTrue(ans)
        ans = self.c1.Inside(self.c4)#c1和c4有两个交点
        self.assertFalse(ans)
        
    def test_Append(self):
        self.c_list = [self.c1] 
        ans = self.c3.Append(self.c_list)
        self.assertTrue(ans)
        ans = self.c4.Append(self.c_list)
        self.assertFalse(ans)

class FucntionTestCase(unittest.TestCase):
    def setUp(self):
        self.c = Circle(0,0,0.8)
        self.c_list = [self.c]
        self.c1 = Circle(0.9,0,0)
        self.c2 = Circle(0.9,0,0.1)
    def test_MaxRadius(self):
        ans = Max_Radius(self.c1,self.c_list)
        self.assertEqual(ans,0.09999999999999998)
        
    def test_Sum(self):
        c_list = [self.c,self.c2]
        ans =  Sum(c_list)
        self.assertEqual(ans, 0.6500000000000001)
        
if __name__ == '__main__':
    unittest.main()
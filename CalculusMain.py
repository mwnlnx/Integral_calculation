import numpy as np

a = input("input lower bound:")
b = input("input upper bound:")
n = int(input("subintervals:"))
fx = input("Input the function:")

class Integral:
    
    def __init__(self,a,b,n,fx):
        
        if isinstance(a,str):
            self.a = eval(a, {"np":np, __builtins__:{}}, {})
        else:
            self.a = float(a)
        
        if isinstance(b,str):
            self.b = eval(b, {"np":np, __builtins__:{}}, {})
        else:
            self.b = float(b)
        
        self.n = n
        self.x = np.linspace(self.a,self.b,self.n)

        if isinstance(fx,str):
            self.fx_left = eval(fx, {"np":np, "x":self.x[:1], __builtins__:{}}, {})
            self.fx_right = eval(fx, {"np":np, "x":self.x[:-1], __builtins__:{}}, {})
        else:
            print("Error in evaluating Function")

    def LeftSum(self):
        dx = (self.b-self.a)/self.n 
        area = self.fx_left * dx
        return sum(area)

    def RightSum(self):
        dx = (self.b-self.a)/self.n
        area = self.fx_right * dx
        return sum(area)
    
    def Trapzoidal(self):
        return (self.LeftSum()+self.RightSum())/2

I = Integral(a,b,n,fx) 
print(I.LeftSum())

         

 
import numpy as np

a = input("input lower bound:")
b = input("input upper bound:")
n = int(input("subintervals:"))
fx_str = input("Input the function:")

class Integral:
    
    def __init__(self,a,b,n,fx_str):
        
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
        self.fx_str = fx_str
        self.dx = (self.b - self.a) / self.n

    def eval_fx(self, x_values):
        return eval(self.fx_str, {"np": np, "x": x_values, "__builtins__": {}}, {})

    def LeftSum(self):
        x_left = np.linspace(self.a, self.b - self.dx, self.n)
        fx_left = self.eval_fx(x_left)
        return sum(fx_left * self.dx)

    def RightSum(self):
        x_right = np.linspace(self.a + self.dx, self.b, self.n)
        fx_right = self.eval_fx(x_right)
        return sum(fx_right * self.dx)
    
    def Midpoint(self):
        x_mid = np.linspace(self.a + self.dx/2, self.b - self.dx/2, self.n)
        fx_mid = self.eval_fx(x_mid)
        return sum(fx_mid * self.dx)
    
    def Trapzoidal(self):
        return (self.LeftSum()+self.RightSum())/2

class Derivative: 

    def __init__(self,a,b,n,fx_str):
        
        if isinstance(a,str):
            self.a = eval(a, {"np":np, __builtins__:{}}, {})
        else:
            self.a = float(a)
        
        if isinstance(b,str):
            self.b = eval(b, {"np":np, __builtins__:{}}, {})
        else:
            self.b = float(b)
        
        self.n = n
        self.fx_str = fx_str

    def eval_fx(self,x_values):
        return eval(self.fx_str, {"np": np, "x": x_values, "__builtins__": {}}, {})
    
    def first_point_derivative(self):
        pass
    
    def second_point_derivative(self):
        pass



I = Integral(a,b,n,fx_str) 

print(f"Left Sum:{I.LeftSum()}, \nRight Sum:{I.RightSum()}, \nMidpoint Sum:{I.Midpoint()}, \nTrapzoidal Sum:0{I.Trapzoidal()}")

         


 
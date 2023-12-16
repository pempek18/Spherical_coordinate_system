import numpy as np
import matplotlib.pyplot as plt
from typing import Literal
class Spherical :
    def __init__(self, print=False) :
        self.is_printing = print 
    var_x = 0
    var_y = 0
    var_z = 0
    var_r = 0
    var_theta = 0
    var_phi = 0 
    
    def _quadrants(self, func:Literal['sin', 'cos', 'tan', 'ctg'], x : float, y : float, z : float = 0) :
        if x==0 and y==0 :
            raise ValueError("Wrong arguments, please type at least arguments x,y,")
        if func not in ['sin', 'cos', 'tan', 'ctg']:
            raise ValueError("Invalid function. Choose from 'sin', 'cos', 'tan', 'ctg'.")
        def _print_Value(value,quadrant,x=0,y=0,z=0) :
            if self.is_printing :
                if x!=0 or y!=0 :
                    print(f"x={x}, y={y}, function={func}, quadrant={quadrant}, value={value}")              
        functions = {'sin':0,
                    'cos':1,
                    'tan' :2,
                    'ctg':3}
        quadrants_values = np.array([[1,1,1,1],
                                    [1,-1,-1,-1],
                                    [-1,-1,1,1],
                                    [-1,1,-1,-1]])
        if x > 0 and y > 0 :
            value = quadrants_values[0,functions[func]] 
            _print_Value(value=value, quadrant=1, x=x, y=y)
            return value
        if x < 0 and y > 0 :
            value = quadrants_values[1,functions[func]]
            _print_Value(value=value, quadrant=2, x=x, y=y)
            return value
        if x < 0 and y < 0 :
            value = quadrants_values[2,functions[func]]
            _print_Value(value=value, quadrant=3, x=x, y=y)             
            return value       
        if x > 0 and y < 0 :
            value = quadrants_values[3,functions[func]]      
            _print_Value(value=value, quadrant=4, x=x, y=y)               
            return value
    def r(self,x,y, z=0) :
        self.var_x = x 
        self.var_y = y 
        self.var_z = z      
        self.var_r = np.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        return self.var_r
    def theta(self,x,y,z = 0) :
        self.var_x = x 
        self.var_y = y 
        self.var_z = z 
        if z != 0 :
            self.var_theta = np.tanh((np.sqrt(pow(x,2) + pow(y,2)) / z )) * self._quadrants('tan', x, y)
        else :
            self.var_theta = 1
        return self.var_theta
    def phi(self,x,y):
        self.var_x = x 
        self.var_y = y 

        if x != 0 :
            phi_quater = 0 
            if x > 0 and y > 0 :
                phi_quater = 0 ; 
            if x < 0 and y > 0 :
                phi_quater = np.pi / 2 
            if x < 0 and y < 0 :
                phi_quater = np.pi 
            if x > 0 and y < 0 :
                phi_quater = np.pi * 3  / 2                             
            self.var_phi = (np.tanh((y / x )) * self._quadrants('tan',x=x,y=y)) + phi_quater
        else:
            if y > 0 :
                self.var_phi = np.tanh(np.pi/2)
            else :
                self.var_phi = np.tanh(np.pi * 3 / 2)
        return self.var_phi
    def x (self, r, theta, phi) :
        self.var_r      = r 
        self.var_theta  = theta 
        self.var_phi    = phi 
        x = r * np.sin(theta) * np.cos(phi)
        return x 
    def y (self,r, theta, phi):
        self.var_r      = r 
        self.var_theta  = theta 
        self.var_phi    = phi      
        y = r * np.sin(theta) * np.sin(phi) 
        return y
    def z (self,r, theta):
        self.var_r      = r 
        self.var_theta  = theta 
        z = r * np.cos(theta)
        return z 
    def plot_data(self) :
        if self.var_z == 0 :
            # Setting the range for x and y axis
            # x_lines = np.linspace(-10, 10, 400)
            # y_lines = np.linspace(-10, 10, 400)

            # Creating the figure and axis
            fig, ax = plt.subplots()

            # Setting the limits for x and y axis
            # ax.set_xlim([-10, 10])
            # ax.set_ylim([-10, 10])

            # Drawing axis lines
            ax.axhline(y=0, color='k')
            ax.axvline(x=0, color='k')

            # Setting grid
            ax.grid(True, which='both')

            # Labeling the axes
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')

            # Title of the graph
            ax.set_title(f"x={self.var_x} y={self.var_y}, z={self.var_z} r={format(self.var_r, '.2f')}, theta={format(self.var_theta,'.2f')}, phi={format(self.var_phi, '.2f')}")
            ax.arrow(0, 0, self.x(self.var_r, self.var_theta, 
            self.var_phi) , self.y(self.var_r, self.var_theta, self.var_phi), head_width=0.2, head_length=0.2, fc='blue', ec='blue')
            ax.scatter(x=self.var_x,y=self.var_y, color='red')
        else :
            # Creating the 3D figure
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.quiver(0, 0, 0, self.x(self.var_r, self.var_theta, self.var_phi), self.y(self.var_r, self.var_theta, self.var_phi), self.z(self.var_r, self.var_theta), color='red')
            ax.scatter(x=self.var_x,y=self.var_y, z=self.var_z)
            # Setting the limits for x, y, and z axis
            # ax.set_xlim([-4, 4])
            # ax.set_ylim([-4, 4])
            # ax.set_zlim([-4, 4])

            # Labeling the axes
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')

            # Title of the graph
            ax.set_title(f"x={self.var_x} y={self.var_y}, z={self.var_z} r={format(self.var_r, '.2f')}, theta={format(self.var_theta,'.2f')}, phi={format(self.var_phi, '.2f')}")

        plt.show()    
if __name__ == '__main__':
    x = float(input("Type x: "))
    y = float(input("type y: ")) 
    z = float(input("type z: "))
    s = Spherical(print=False)
    r       = s.r(x,y,z)
    theta   = s.theta(x=x,y=y,z=z)
    phi     = s.phi(x=x,y=y)
    print(f"x={x} y={y}, z={z} r={format(r, '.2f')}, theta={format(theta,'.2f')}, phi={format(phi, '.2f')}")
    s.plot_data()

import numpy as np
import matplotlib.pyplot as plt
from typing import Literal
class Spherical :
    def __init__(self, print=False) :
        self.is_printing = print 
    __var_x : float = 0
    __var_y : float = 0
    __var_z : float = 0
    __var_r : float = 0
    __var_theta : float = 0
    __var_phi   : float = 0 
    
    def _quadrants(self, func:Literal['sin', 'cos', 'tan', 'ctg'], x : float, y : float ) :
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
        else :
            return 1 
    def r(self,x : float,y : float, z : float=0) :
        self.__var_x = x 
        self.__var_y = y 
        self.__var_z = z      
        self.__var_r = np.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        return self.__var_r
    def theta(self,x : float,y : float,z : float = 0) :
        self.__var_x = x 
        self.__var_y = y 
        self.__var_z = z 
        if z != 0 :
            self.__var_theta = np.arctan((np.sqrt(pow(x,2) + pow(y,2)) / z )) 
        elif x * y >= 0 :
            self.__var_theta = np.pi / 2
        elif x * y < 0 :
            self.__var_theta = -np.pi / 2
        return self.__var_theta
    def theta_r(self,r : float, z : float) :
        self.__var_r = r 
        self.__var_z = z
        if z == 0 :
            self.__var_theta = np.pi / 2 
        return self.__var_theta
    def phi(self,x : float,y : float):
        self.__var_x = x 
        self.__var_y = y 

        if x != 0 and y != 0:
            phi_quater = 0  
            #first quater
            if x > 0 and y > 0 :
                phi_quater = 0 ; 
            #secound quater
            if x < 0 and y > 0 :
                phi_quater = np.pi
            #third quater
            if x < 0 and y < 0 :
                phi_quater = np.pi 
            #forth quater
            if x > 0 and y < 0 :
                phi_quater =  np.pi * 2              
            print("tan in quater: ", self._quadrants('tan',x=x,y=y), "phi quater: ", phi_quater)               
            self.__var_phi = (np.arctan(y / x ) + phi_quater) #* self._quadrants('tan',x=x,y=y)
        else:
            if x==0 and y > 0 :
                self.__var_phi = np.pi/2
            elif x ==0 and y < 0 :
                self.__var_phi = np.pi * 3 / 2
            elif x > 0 and y == 0 :
                self.__var_phi = 0
            elif x < 0 and y==0 :
                self.__var_phi = np.pi
        return self.__var_phi
    def x (self, r : float, theta : float, phi : float) :
        self.__var_r      = r 
        self.__var_theta  = theta 
        self.__var_phi    = phi 
        x = r * np.sin(theta) * np.cos(phi) * (1 if (theta > 0) else -1)
        return x 
    def y (self,r : float, theta : float, phi : float):
        self.__var_r      = r 
        self.__var_theta  = theta 
        self.__var_phi    = phi      
        y = r * np.sin(theta) * np.sin(phi) * (1 if (theta > 0) else -1)
        return y
    def z (self,r : float, theta : float):
        self.__var_r      = r 
        self.__var_theta  = theta 
        z = r * np.cos(theta) * (1 if (theta >= 0) else -1)
        return z 
    def plot_data(self) :
        #ploting data count againg to double check the calculations
        x_to_plot = self.x(self.__var_r, self.__var_theta, self.__var_phi)
        y_to_plot = self.y(self.__var_r, self.__var_theta, self.__var_phi)
        z_to_plot = self.z(self.__var_r, self.__var_theta)
        title = f"""
        setpoint    : x={format(self.__var_x, '.2f')} y={format(self.__var_y, '.2f')}, z={format(self.__var_z, '.2f')}
        spherical   : r={format(self.__var_r, '.2f')}, theta={format(self.__var_theta,'.2f')}, phi={format(self.__var_phi, '.2f')}
        recalulated: x={format(x_to_plot, '.2f')}, y={format(y_to_plot, '.2f')}, z={format(z_to_plot, '.2f')} """
        if self.__var_z == 0 :
            # Creating the figure and axis
            fig, ax = plt.subplots()

            # Drawing axis lines
            ax.axhline(y=0, color='k')
            ax.axvline(x=0, color='k')

            # Setting grid
            ax.grid(True, which='both')

            # Labeling the axes
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')

            ax.arrow(x=0, y=0, 
                     dx=x_to_plot, 
                     dy=y_to_plot, 
                     head_width=0, 
                     head_length=0, 
                     fc='blue', 
                     ec='blue',
                     label='recarculated x y')
            ax.scatter(x=self.__var_x,y=self.__var_y, color='red', label='setpoint')
        else :
            # Creating the 3D figure
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.quiver(0, 0, 0, x_to_plot, y_to_plot, z_to_plot, color='red', label='recalulated x y')
            ax.scatter(xs=self.__var_x,ys=self.__var_y, zs=self.__var_z, label='setpoint')

            # Labeling the axes
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')
        plt.title(title, fontsize=11, pad=-20, loc='left')
        plt.show()    
if __name__ == '__main__':
    while(True):
        x = float(input("Type x: ").replace(',','.'))
        y = float(input("type y: ").replace(',','.')) 
        z = float(input("type z: ").replace(',','.'))
        s = Spherical(print=True)
        r       = s.r(x,y,z)
        theta   = s.theta(x=x,y=y,z=z)
        phi     = s.phi(x=x,y=y)
        print(f"x={x} y={y}, z={z} r={format(r, '.2f')}, theta={format(theta,'.2f')}, phi={format(phi, '.2f')}")
        s.plot_data()
        exit = input("repeat ? y/n :")
        if exit != "y" :
            break
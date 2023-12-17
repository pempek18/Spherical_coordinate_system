# Spherical_coordinate_system
Python class Spherical provides possibility to calculate cartesian points to Spherical and plot it. 

![Alt text](./data//Figure_1.png?raw=true "3D Printed Spherical arrow")

![Alt text](./data//Figure_2.png?raw=true "Printed Spherical arrow")

examples of class usage : 
    x = float(input("Type x: "))
    y = float(input("type y: ")) 
    z = float(input("type z: "))
    s = Spherical(print=True)
    r       = s.r(x,y,z)
    theta   = s.theta(x=x,y=y,z=z)
    phi     = s.phi(x=x,y=y)
    print(f"x={x} y={y}, z={z} r={format(r, '.2f')}, theta={format(theta,'.2f')}, phi={format(phi, '.2f')}")
    s.plot_data()


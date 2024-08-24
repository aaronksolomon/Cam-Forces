## Totem Cams

#### Contributed by chortbauer 

In Totem Cams the load path from the climber/rope to the cam is different to the "standard" cams.

In standard cams, the force is transmitted through the axle on which the cams pivot.
Whereas in Totem cams, the cables are directly connected to the cams. The axle only transmits forces between the individual cams.

The geometry of the different load path, leads to an increased normal force compared to standard cams. The increase depends on the ratio of the two log spirals that are present on every Totem Cam cam. The spiral over which the cable is routed (B) and the spiral that touches the rock (C).

Very good source with drawings and calculations (directly from Totem): [TotemCam_Mechanical_Principles.pdf]([url](https://www.totemmt.com/wp-content/uploads/2018/09/TotemCam_Mechanical_Principles.pdf))

I worked through the parallel crack formulas myself and got the same results as in the linked pdf. 

My conclusions:
Totem cams can tolerate a lower coefficient of friction at the same camming angle. 
They "pay" for this with increased normal forces compared to standard cams. This could lead to a lower max load capacity, as the cams and the axle have to resist the higher normal forces.
From the geometry follows that the normal force increase has to be smaller than a factor of 2: 1 < F_n_totem / F_n < 2

Theoretically, they could also use a steeper cam angle with the same friction limits as standard cams. This would maybe allow the cam to fit inside a wider range of crack thicknesses.

Disclaimer: I'm a mechanical engineer with **zero** climbing experience.

I expanded one of your plots:
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
theta = np.radians(14.5)  # Example angle in degrees, convert to radians

# Force range (F_p) from 1 kN to 12 kN
F_p = np.linspace(2e3, 12e3, 100)  # Force in Newtons

# Calculate F_c,x and F_c,y
F_c_x = F_p / (2 * np.tan(theta))  # F_c,x as a function of F_p
F_c_x_Totem = F_p * (1+b_c.value) / (2 * np.tan(theta))  # F_c,x as a function of F_p
F_c_y = F_p / 2  # F_c,y as a function of F_p

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(F_p / 1e3, F_c_x / 1e3, label=r'$F_{c,x}$ (Outward Component)', color='blue')
plt.plot(F_p / 1e3, F_c_x_Totem / 1e3, label=r'$F_{c,x,Totem}$ (Outward Component) $b/c = 0.6$', color='green')
plt.plot(F_p / 1e3, F_c_y / 1e3, label=r'$F_{c,y}$ (Downward Component)', color='orange')
plt.xlim(2, 13)  # Set x-axis limits 
plt.ylim(0, 25)  # Set y-axis limits 
plt.xlabel('Applied Force $F_p$ (kN)')
plt.ylabel('Force Components (kN)')
plt.title(r'Force Components $F_{c,x}$ and $F_{c,y}$  as Functions of $F_p$ for $\theta = 14.5^\circ$')
plt.legend()
plt.grid(True)
plt.gca()
```

And created a very simple additional one that shows the increase in normal force depending on the cam size ratio.
```python
import numpy as np
import matplotlib.pyplot as plt

# Range for Ration b/c
b_c = np.linspace(0,1,100)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(b_c, 1 + b_c, color='blue')
plt.xlabel('Ratio $b \\: / \\: c$')
plt.ylabel('Ratio $F_{c,x,Totem} \\: / \\: F_{c,x}$')
plt.title(r'Ratio of normal Force Components $F_{c,x,Totem} \: / \: F_{c,x}$  as a Functions of Totem Cam Ratio $b \: / \: c$')
plt.grid(True)
plt.gca()
```
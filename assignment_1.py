# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1olnEYN2-Y3-EZme5EldzCKZ4UF-ZJbMq
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.sqrt(3)
#creating points to plot motion of projectile
x1 = np.linspace(0,3,300)
x2 = np.linspace(0,2*a,300)
#for equation of motion using y=xtanA(1-x/R),R is the range of projectile 
#for the given circumstances value of A for 'R' is 30 degrees and for 'R_max' is 45 degrees
#tan(30)=1/sqrt(3) =1/a ,tan(45)=1
y1 = x1*(1/a)*(1-(x1/3))
y2 = x2*1*(1-(x2/(2*a)))

# Create the plot
plt.plot(x1,y1,label='R')
plt.plot(x2,y2,label='R_max')
plt.title('Motion of bullet comparing R and R_max')
plt.xlabel('Range(in km)')
plt.ylabel('Heigth(in km)')
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.show()
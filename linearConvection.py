

import numpy as np
import time,sys

# solving du/dt+c*du/dx =0

nx = 41
dx = 2/(nx-1)
nt = 25 #time steps
dt = 0.025 #amount of time each time step covers
c=1 #wavespeed

u = np.ones(nx) #vector of 1's length nx

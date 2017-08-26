import numpy as np
import matplotlib.pyplot as plt
import math as math

#---------Setting the seed of the generator to get consistent test--------------
np.random.seed(10)

#---------Setting the problem paramaters that suite the problem-----------------
ntime = 10000
nreal = 10000

stepright = 1
stepleft =  -1

pright = float(0.6)
pleft = float(0.4)

#---------Creating an (1000,) with random integers from (0-9)-------------------
d0 = np.random.randint(0,10,(nreal,ntime))

#------------Changing the values of d0 to get weighted movements----------------
d0[d0 < 6] = stepright
d0[d0 >= 6] = stepleft

testd0 = np.insert(d0,0,0,axis=1)

#-----------------------Calulating the mean-------------------------------------
test1 = np.cumsum(testd0,axis = 1)

nt = np.arange(ntime+1)

avg = np.sum(test1, axis = 0)/float(nreal)

distavg = nt*(2*(.6) - 1)

#-----------------------Square mean value---------------------------------------
sqavg = np.sum(test1**2, axis = 0)/float(ntime)

#-----------------------Calulating the Variance---------------------------------
var = sqavg - avg**2

distvar = np.square(nt)*(4*(pright**2) - 4*pright + 1) + 4*nt*pright*pleft - np.square(distavg)

#---------------------Creating and saving the plot------------------------------
fig = plt.figure(1, figsize = (5.0,5.0))

#--------------------Plotting a sample path for reference of walk---------------
plt.subplot(211)
plt.title('1D Random Walk 1st Path', fontsize=14)
plt.xlabel('Step #', fontsize = 12)
plt.ylabel('Position', fontsize = 12)
plt.plot(test1[1], 'm')

#-------------------Plotting the mean/var from data and distrbutions------------
plt.subplot(212)
plt.title('AVG/VAR(from data), AVG/VAR from dist.', fontsize=14)
plt.xlabel('Step #', fontsize = 12)
plt.ylabel('Position', fontsize = 12)
plt.plot(avg,'r')
plt.plot(var,'b')
plt.plot(distavg, 'r--')
plt.plot(distvar, 'b--')

#-----------------------------adjusting subplots--------------------------------
plt.subplots_adjust(hspace=0.5, wspace=0.1)
#plt.show()
#-----------------------------Saving the figure---------------------------------
fig.savefig("/Users/Parker/Desktop/Walks/Newplots/1DRW10000WNew.png", format = "png", dpi=800)

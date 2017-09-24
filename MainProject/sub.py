
import matplotlib.pyplot as plt

fig=plt.figure()

x=[1,3,4,6,7]
y=[2,3,5,6,9]

#ax1=fig.add_subplot(221)
#ax2=fig.add_subplot(222)
#ax3=fig.add_subplot(212)



ax1=plt.subplot2grid((6,1),(0,0),rowspan=1,colspan=1)
ax2=plt.subplot2grid((6,1),(1,0),rowspan=4,colspan=1)
ax3=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)

ax1.plot(x,y,'r--')
ax2.plot(x,y)
ax3.plot(x,y)

plt.show()



##import pylab as plt
##
##fig = plt.figure()
##ax1 = fig.add_subplot(121)
##ax2 = fig.add_subplot(122)
##
##def get_axis_limits(ax, scale=.9):
##    return ax.get_xlim()[1]*scale, ax.get_ylim()[1]*scale
##
##ax1.annotate('A',xy=1)
##ax2.annotate('B',xy=2)
##plt.show()

import matplotlib.pyplot as plt
from newfor import houtem,houtim,namcty,houpre,houhumi

def grapy(city,x,y,z):
    
    print(type(city),type(x))
    namcty(str(city))
    ht=houtem(int(x),int(y),int(z))#x=ht
    hti=houtim(int(x),int(y),int(z))#y=hti
    hp=houpre(int(x),int(y),int(z))#z=hp
    q=houhumi(int(x),int(y),int(z))
    #plt.plot(y,x,label='first')

    #plt.plot(y,z,label='second')

    ##
    ##fig=plt.figure()
    ##ax1=fig.add_subplot(221,label='sdf')
    ##ax2=fig.add_subplot(222,label='sdf')
    ##ax3=fig.add_subplot(223,label='dfg')
    ##ax4=fig.add_subplot(224,label='sdf')

    ax1=plt.subplot2grid((6,1),(0,0),rowspan=1,colspan=1)
    ax2=plt.subplot2grid((6,1),(1,0),rowspan=4,colspan=1)
    ax3=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)

    plt.xlabel('Time')

    #plt.ylabel('important')
    #plt.title('interesting graph\nCheck it out')
    plt.legend()
    print (z)
    ax1.plot(hti,q,'r--',label='temp')
    ax2.plot(hti,ht,'bs')
    ax3.plot(hti,hp,'g^')
    ##ax4.plot(y,x,'bs')

    ax1.set_ylabel('Humidity')
    ax2.set_ylabel('Temperature')
    ax3.set_ylabel('Pressure')
    ##ax3.set_ylabel('assdxaf')

    ax1.get_xaxis().set_visible(False)
    ax2.get_xaxis().set_visible(False)
    ##ax3.get_xaxis().set_visible(False)

    plt.show()

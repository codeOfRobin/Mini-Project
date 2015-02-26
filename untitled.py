from numpy import *
import matplotlib.pyplot as plt
a=arange(16).reshape(2,8)
a.reshape(4,4)
print "{}".format(a.dtype)

b=array([(2,4,6,7),(32,5,67,7)]) 
print "{}".format(b)

c=arange(3,4,0.2)
print "{}".format(c)

x=linspace(0,2*pi,100)
f=sin(x)
plt.plot(f,x)
plt.show()
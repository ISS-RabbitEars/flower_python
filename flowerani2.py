import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

p=1
r=5
n=5
e=2
f=60
fig, a=plt.subplots()
fig.patch.set_facecolor('xkcd:black')

def run(frame):
	if frame<=f:
		plt.clf()
		th=np.linspace(0,2*np.pi*(frame)/f,100)
		x=(p+r*np.cos(n*th/2)**e)*np.cos(th)
		y=(p+r*np.cos(n*th/2)**e)*np.sin(th)
		plt.plot(x,y,'r',linewidth=10)
		plt.xlim([-6,7])
		plt.ylim([-6,6])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>f:
		circle = plt.Circle((0,0), radius=1, fc='y')
		ax=plt.gca()
		ax.add_patch(circle)
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
ani=animation.FuncAnimation(fig,run,frames=2*f)
writervideo = animation.FFMpegWriter(fps=10)
ani.save('flower2.gif', writer=writervideo)
plt.show()

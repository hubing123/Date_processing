import numpy as np
import matplotlib.pyplot as plt
import random
# points=np.arange(-5,5,0.01)
# xs,ys=np.meshgrid(points,points)
# z=np.sqrt(xs**2+ys**2)
# plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
# plt.title("Image plot of ")
# plt.show()

position=0
walk=[position]
steps=1000
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)
plt.plot(walk)
plt.show()
# Animation of 3d Random Walk (Square Lattice model)

import matplotlib.pyplot as plt
from matplotlib import animation
import randomWalk_3dSquareLatticeFunc as rdwalk

N = 200
M = 3
imgs_rep = []

fig_title = "3-dimensional Random Walk (N = "+str(N)+")"
plot_lim = 15

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='X', ylabel='Y', zlabel='Z',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim], zlim=[-plot_lim , plot_lim], 
        projection='3d')
#ax.grid(axis='both', color="gray", lw=0.5)

for m in range(M):
    imgs = rdwalk.randomWalk_3dSquareLattice(N)
    imgs_rep = imgs_rep + imgs
    print("repeat num = "+str(m+1))

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('./gif/randomWalk_3dSquareLattice.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()

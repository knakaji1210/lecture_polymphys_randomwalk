# Animation of 2d Random Walk (Square Lattice model)

import matplotlib.pyplot as plt
from matplotlib import animation
import randomWalk_2dSquareLatticeFunc as rdwalk

N = 100
M = 5
imgs_rep = []

fig_title = "2-dimensional Random Walk (N = "+str(N)+")"
plot_lim = 30

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='X', ylabel='Y',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

for m in range(M):
    imgs = rdwalk.randomWalk_2dSquareLattice(N)
    imgs_rep = imgs_rep + imgs
    print("repeat num = "+str(m+1))

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('./gif/randomWalk_2dSquareLattice.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()

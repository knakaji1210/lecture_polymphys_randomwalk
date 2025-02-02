# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import randomWalk_2dSquareLatticeFunc_v1 as rdwalk

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    M = int(input('Number of repetition (default=5): '))
except ValueError:
    M = 5

imgs_rep = []

fig_title = "2-dimensional Random Walk ($N$ = {0})".format(N)
plot_lim = 2*np.sqrt(N)

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

for m in range(M):
    imgs = rdwalk.randomWalk_2dSquareLattice(N)
    imgs_rep = imgs_rep + imgs
    print("repeat num = {0}".format(m+1))

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('./gif/randomWalk_2dSquareLattice.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()

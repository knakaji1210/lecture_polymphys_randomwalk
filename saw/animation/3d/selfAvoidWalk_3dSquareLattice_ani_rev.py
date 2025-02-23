# Animation of 3d Self-Avoiding Walk Walk (Square Lattice model)
# 1d, 2dではmatplotlibのanimationからanimatplotに置き換える試みを行ったが、
# animatplotが3dに対応してないため、過去に作成したバージョンのままキープする。

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import selfAvoidWalk_3dSquareLatticeFunc as sawalk

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    M = int(input('Number of repetition (default=5): '))
except ValueError:
    M = 5

imgs_rep = []

fig_title = "3-dimensional Self-Avoiding Walk ($N$ = {0})".format(N)
plot_lim = 1.5*np.sqrt(N)

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$', zlabel='$Z$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim], zlim=[-plot_lim , plot_lim],
        projection='3d')
#ax.grid(axis='both', color="gray", lw=0.5)

for m in range(M):
    imgs = sawalk.selfAvoidWalk_3dSquareLattice(N)
    imgs_rep = imgs_rep + imgs
    print("repeat num = {0}".format(m+1))

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('./gif/selfAvoidWalk_3dSquareLattice.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()

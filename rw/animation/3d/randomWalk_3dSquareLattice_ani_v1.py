# Animation of 3d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import randomWalk_3dSquareLatticeFunc_v1 as rdwalk
import time     # added in 250211

try:
    N = int(input('Degree of polymerization (default=100): '))
except ValueError:
    N = 100

try:
    M = int(input('Number of repetition (default=3): '))
except ValueError:
    M = 3

start_time = time.process_time()     # added in 250211

imgs_rep = []

fig_title = "3-dimensional Random Walk ($N$ = {0})".format(N)
plot_lim = np.sqrt(N)

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$', zlabel='$Z$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim], zlim=[-plot_lim , plot_lim], 
        projection='3d')
#ax.grid(axis='both', color="gray", lw=0.5)

for m in range(M):
    imgs = rdwalk.randomWalk_3dSquareLattice(N)
    imgs_rep = imgs_rep + imgs
    print("repeat num = {0}".format(m+1))

end_time = time.process_time()                              # added in 250211
elapsed_time = end_time - start_time                        # added in 250211
print("elapsed time = {0:.3f} sec".format(elapsed_time))    # added in 250211

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('./gif/randomWalk_3dSquareLattice.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()

# Animation of 3d Random Walk (Square Lattice model)
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250211）

# animatplotは3次元描画はできないので、とりあえず(x-y)面、(x-z)面の投影を描かせることにする

# 計測結果
# N = 100, M = 5で
# v1 = 0.541 s
# v2 = 0.084 s

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import time
import randomWalk_3dSquareLatticeFunc_v2 as rdwalk

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    M = int(input('Number of repetition (default=5): '))
except ValueError:
    M = 5

start_time = time.process_time()                              # 計算にかかる時間を計測

x_array_steps_m, y_array_steps_m, z_array_steps_m, x_front_m, y_front_m, z_front_m, x_end_m, y_end_m, z_end_m = rdwalk.randomWalk_3d_M(N,M)

fig1_title = "3-dimensional Random Walk (x-y projection) ($N$ = {0}, $M$ = {1})".format(N,M)
fig2_title = "3-dimensional Random Walk (x-z projection) ($N$ = {0}, $M$ = {1})".format(N,M)
plot_lim = 2*np.sqrt(N)

fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(121, title=fig1_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax1.grid(axis='both', color="gray", lw=0.5)
ax2 = fig.add_subplot(122, title=fig2_title, xlabel='$X$', ylabel='$Z$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax2.grid(axis='both', color="gray", lw=0.5)

randomWalk_xy = amp.blocks.Line(x_array_steps_m, y_array_steps_m, ax=ax1, ls='-', c='cyan', zorder=1)
randomWalk_front_xy = amp.blocks.Scatter(x_front_m, y_front_m, ax=ax1, marker="x", c='black', zorder=1)
randomWalk_end_xy = amp.blocks.Scatter(x_end_m, y_end_m, ax=ax1, marker="o", c='red', zorder=3)

randomWalk_xz = amp.blocks.Line(x_array_steps_m, z_array_steps_m, ax=ax2, ls='-', c='cyan', zorder=1)
randomWalk_front_xz = amp.blocks.Scatter(x_front_m, z_front_m, ax=ax2, marker="x", c='black', zorder=1)
randomWalk_end_xz = amp.blocks.Scatter(x_end_m, z_end_m, ax=ax2, marker="o", c='red', zorder=3)

timeArray = rdwalk.timeArray(N,M)
timeLine = amp.Timeline(timeArray, units=' steps', fps=10)

anim = amp.Animation([randomWalk_xy,randomWalk_front_xy,randomWalk_end_xy, randomWalk_xz,randomWalk_front_xz,randomWalk_end_xz], timeLine)
anim.controls()

end_time = time.process_time()                              # 計算にかかる時間を計測
elapsed_time = end_time - start_time                        # 計算にかかる時間を計測
print("elapsed time = {0:.3f} sec".format(elapsed_time))    # 計算にかかる時間を表示

savefile = "./gif/randomWalk_3d_N{0}_M{1}".format(N,M)
anim.save_gif(savefile)

plt.show()
plt.close()

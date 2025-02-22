# Animation of 2d Random Walk
# matplotlibのanimationからanimatplotに置き換える試み（250219）

import numpy as np
import rw2dFunc_square_v3 as rw
import matplotlib.pyplot as plt
import animatplot as amp
import time

try:
    N = int(input('Degree of polymerization (default=100): '))
except ValueError:
    N = 100

try:
    M = int(input('Number of repetition (default=3): '))
except ValueError:
    M = 3

start_time = time.process_time()                              # 計算にかかる時間を計測

x_list_steps_m, y_list_steps_m, x_front_m, y_front_m, x_end_m, y_end_m = rw.rw2dM(N,M)

fig_title = "2-dimensional Random Walk ($N$ = {0}, $M$ = {1})".format(N,M)
plot_lim = 2*np.sqrt(N)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(x_list_steps_m, y_list_steps_m, ax=ax, ls='-', c='cyan', zorder=1)
randomWalk_front = amp.blocks.Scatter(x_front_m, y_front_m, ax=ax, marker="x", c='black', zorder=1)
randomWalk_end = amp.blocks.Scatter(x_end_m, y_end_m, ax=ax, marker="o", c='red', zorder=3)

timeList = rw.timeList(N,M)
timeLine = amp.Timeline(timeList, units=' steps', fps=10)

anim = amp.Animation([randomWalk,randomWalk_front,randomWalk_end], timeLine)
anim.controls()

end_time = time.process_time()                              # 計算にかかる時間を計測
elapsed_time = end_time - start_time                        # 計算にかかる時間を計測
print("elapsed time = {0:.3f} sec".format(elapsed_time))    # 計算にかかる時間を表示

savefile = "./gif/randomWalk_2d_N{0}_M{1}".format(N,M)
anim.save_gif(savefile)

plt.show()
plt.close()

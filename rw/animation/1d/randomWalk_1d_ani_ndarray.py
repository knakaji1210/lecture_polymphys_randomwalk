# Animation of 1d Random Walk
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250209）

# 計測結果
# N = 100, M = 5で
# v1 = 0.163 s
# v2 = 0.086 s

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import time
import randomWalk_1dFunc_v2 as rdwalk

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    M = int(input('Number of repetition (default=5): '))
except ValueError:
    M = 5

start_time = time.process_time()                              # 計算にかかる時間を計測

x_array_steps_m, y_array_steps_m, x_front_m, y_front_m, x_end_m, y_end_m = rdwalk.randomWalk_1d_M(N,M)

fig_title = "1-dimensional Random Walk ($N$ = {0}, $M$ = {1})".format(N,M)
plot_lim = 2*np.sqrt(N)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(x_array_steps_m, y_array_steps_m, ax=ax, ls='-', c='cyan', zorder=1)
randomWalk_front = amp.blocks.Scatter(x_front_m, y_front_m, ax=ax, marker="x", c='black', zorder=1)
randomWalk_end = amp.blocks.Scatter(x_end_m, y_end_m, ax=ax, marker="o", c='red', zorder=3)

timeArray = rdwalk.timeArray(N,M)
timeLine = amp.Timeline(timeArray, units=' steps', fps=10)

anim = amp.Animation([randomWalk,randomWalk_front,randomWalk_end], timeLine)
anim.controls()

end_time = time.process_time()                              # 計算にかかる時間を計測
elapsed_time = end_time - start_time                        # 計算にかかる時間を計測
print("elapsed time = {0:.3f} sec".format(elapsed_time))    # 計算にかかる時間を表示

savefile = "./gif/randomWalk_1d_N{0}_M{1}".format(N,M)
anim.save_gif(savefile)

plt.show()
plt.close()

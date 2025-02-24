# Figure Drawing 

import matplotlib.pyplot as plt

def figDraw(fig, row, col, order, fig_title, x_label, y_label, x_range, y_range, x_list, y_list, xi, yi, xt, yt):

    location = str(row)+str(col)+str(order)

    ax = fig.add_subplot(int(location),title=fig_title, xlabel=x_label, ylabel=y_label,
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
    ax.grid(axis='both', color="gray", lw=0.5)
    ax.plot(x_list, y_list)
    ax.plot(xi, yi, marker=".", color="red")
    ax.plot(xt, yt, marker=".", color="red")

    return
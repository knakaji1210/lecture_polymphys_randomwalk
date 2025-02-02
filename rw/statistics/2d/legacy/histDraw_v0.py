# Histgram Drawing 

import numpy as np
import matplotlib.pyplot as plt

def histDraw(fig, row, col, order, hist_title, hist_color, input_list):

    num_bins = 50

    location = str(row)+str(col)+str(order)

    ax = fig.add_subplot(int(location),title=hist_title)
    hist = plt.hist(input_list, bins=num_bins, color=hist_color, density=True)
    histMin, histMax = plt.xlim()
    binWidth = (histMax - histMin) / num_bins
    hist_Y = np.array(hist[0])
    hist_X = np.array(hist[1])
    histInfo = [histMin, histMax, binWidth]

    return hist_X, hist_Y, histInfo
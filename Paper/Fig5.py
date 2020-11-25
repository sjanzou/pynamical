import pynamical
from pynamical import simulate, bifurcation_plot, save_fig
import pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.cm as cm

title_font = pynamical.get_title_font()
label_font = pynamical.get_label_font()
pops = simulate(num_gens=20, rate_min=0.6, rate_max=3.6, num_rates=7)
pops.applymap(lambda x: '{:03.3f}'.format(x))

def get_colors(cmap, n, start=0., stop=1., alpha=1., reverse=False):
    '''return n-length list of rgba colors from the passed colormap name and alpha,
       limit extent by start/stop values and reverse list order if flag is true'''
    colors = [cm.get_cmap(cmap)(x) for x in np.linspace(start, stop, n)]
    colors = [(r, g, b, alpha) for r, g, b, _ in colors]
    return list(reversed(colors)) if reverse else colors

color_list = get_colors('viridis', n=len(pops.columns), start=0., stop=1)
for color, rate in reversed(list(zip(color_list, pops.columns))):
    ax = pops[rate].plot(kind='line', figsize=[10, 6], linewidth=2.5, alpha=0.95, c=color)
ax.grid(True)
ax.set_ylim([0, 1])
ax.legend(title='Growth Rate', loc=3, bbox_to_anchor=(1, 0.525))
ax.set_title('Logistic Model Results by Growth Rate', fontproperties=title_font)
ax.set_xlabel('Generation', fontproperties=label_font)
ax.set_ylabel('Population', fontproperties=label_font)

save_fig('logistic-map-growth-rates')
plt.show()
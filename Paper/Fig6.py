import pynamical
from pynamical import simulate, bifurcation_plot, save_fig
import pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.cm as cm

pops = simulate(num_gens=100, rate_min=0., rate_max=4.0, num_rates=200, num_discard=100)
bifurcation_plot(pops, xmax=4.0, filename='logistic-map-bifurcation-6')
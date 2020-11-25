import pynamical
from pynamical import simulate, bifurcation_plot, save_fig
import pandas as pd, numpy as np,  matplotlib.pyplot as plt, matplotlib.cm as cm

# run the logistic model for 20 generations for 7 growth rates between 0.5 and 3.5 then view the output
pops = simulate(num_gens=20, rate_min=0.6, rate_max=3.6, num_rates=7)
pops.applymap(lambda x: '{:03.3f}'.format(x))

print (pops)

pops.to_csv("C:/Projects/GitHub/sjanzou/pynamical/Paper/out3.6.csv", sep=',')



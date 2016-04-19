""" Calculates Bayesian Probabilty that A - B > x

Usage:
  ab_test.py <a_population> <a_success> <b_population> <b_success>
             [--sample_size=<n>] [--absolute_effect_size=<x> | --relative_effect_size=<x>]
             [--alpha=<a>] [--beta=<b>]

Options:
  --sample_size=<n>   Select a sample size [default: 10000]
  --absolute_effect_size=<x>   Select the absolute size of effect to be detected [default: 0.0]
  --relative_effect_size=<x>   Select the relative size of effect to be detected
  --alpha=<a>         Select an alpha [default: 1.0]
  --beta=<b>          Select a beta [default: 1.0]

"""
from docopt import docopt
from numpy.random import beta as beta_dist
import numpy


arguements = docopt(__doc__)

a_population = int(arguements['<a_population>'])
b_population = int(arguements['<b_population>'])
a_success = int(arguements['<a_success>'])
b_success = int(arguements['<b_success>'])
sample_size = int(arguements['--sample_size'])
absolute_effect_size = float(arguements['--absolute_effect_size'])
if arguements['--relative_effect_size']:
    relative_effect_size = float(arguements['--effect_size'])
else:
    relative_effect_size = None

alpha = float(arguements['--alpha'])
beta = float(arguements['--beta'])

a_samples = beta_dist(a_success+alpha, a_population-a_success+beta, sample_size)
b_samples = beta_dist(b_success+alpha, b_population-b_success+beta, sample_size)

if relative_effect_size:
    print numpy.mean((a_samples - b_samples)/b_samples > relative_effect_size)
else:
    print numpy.mean((a_samples - b_samples) > absolute_effect_size)

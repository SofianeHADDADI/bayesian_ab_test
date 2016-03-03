""" Calculate Bayesian Probabilty that A > B

Usage:
  ab_test.py <a_population> <a_success> <b_population> <b_success> [--sample_size=<n>] [--alpha=<a>] [--beta=<b>]

Options:
  --sample_size=<n>   Select a sample size [default: 10000]
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
alpha = float(arguements['--alpha'])
beta = float(arguements['--beta'])

a_samples = beta_dist(a_success+alpha, a_population-a_success+beta, sample_size)
b_samples = beta_dist(b_success+alpha, b_population-b_success+beta, sample_size)

print numpy.mean(a_samples > b_samples)

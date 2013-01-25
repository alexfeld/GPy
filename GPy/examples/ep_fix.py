# Copyright (c) 2012, GPy authors (see AUTHORS.txt).
# Licensed under the BSD 3-clause license (see LICENSE.txt)


"""
Simple Gaussian Processes classification
"""
import pylab as pb
import numpy as np
import GPy
pb.ion()

default_seed=10000

model_type='Full'
inducing=4
seed=default_seed
"""Simple 1D classification example.
:param model_type: type of model to fit ['Full', 'FITC', 'DTC'].
:param seed : seed value for data generation (default is 4).
:type seed: int
:param inducing : number of inducing variables (only used for 'FITC' or 'DTC').
:type inducing: int
"""
data = GPy.util.datasets.toy_linear_1d_classification(seed=seed)
likelihood = GPy.inference.likelihoods.probit(data['Y'][:, 0:1])

m = GPy.models.GP(data['X'],likelihood=likelihood)

m.constrain_positive('var')
m.constrain_positive('len')
m.tie_param('lengthscale')
m.approximate_likelihood()
print m.checkgrad()
# Optimize and plot
m.optimize()
#m.em(plot_all=False) # EM algorithm
m.plot()

print(m)
